#!/usr/bin/env python3
# author: @netmanchris

""" Copyright 2015 Hewlett Packard Enterprise Development LP

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   """

# This section imports required libraries
import requests
import json
import sys
import time
import subprocess
import csv
import os
import ipaddress
import pysnmp
from requests.auth import HTTPDigestAuth
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902

cmdGen = cmdgen.CommandGenerator()


# IMC Device Class

class IMCDev:
    """
    imc_dev class takes in the ip_address which is used as the primary key to gather the following attributes
         for a device which as been previously discovered in the HP IMC Network Management platform.
         Each instance of this class should have the following attributes

         ip: The IP address used to manage the device in HP IMC
         description: returns the description of the device as discovered in HP IMC
         location: returns the location of the device as discovered in HP IMC
         contact: returns the contact of the device as discovered in HP IMC
         type: returns the type of the device as discovered in HP IMC
         name: returns the name of the device as discovered in HP IMC
         status: returns the current alarm status as discovered in HP IMC
         devid: returns the current devid used to internally identify the device as discovered in HP IMC
         interfacelist: returns the current list of interfaces for the device as discovered in HP IMC
         numinterface: returns a count of the number of interfaces in the interfacelist attribute
         vlans: returns the current vlans existing in the device as discovered in HP IMC. Device must be supported in the
                HP IMC Platform VLAN manager module.
         accessinterfaces: returns the device interfaces configured as access interfaces. Device must be supported in the
                HP IMC Platform VLAN manager module.
         trunkinterfaces: returns the device interfaces configured as trunk interfaces. Device must be supported in the
                HP IMC Platform VLAN manager module.
         alarm: returns the current unrecovered alarms as known by HP IMC.
         num alarms: returns a count of the number of alarms as returned by the alarm attribute
         serial: returns the network assets, including serial numbers for the device as discovered by HP IMC. The device
                must support the ENTITY MIB ( rfc 4133 ) for this value to be returned.
         runconfig: returns the most recent running configuration for the device as known by HP IMC. The device must be
                be supported in the HP IMC platform ICC module.
         startconfig: returns the most recent startup configuration for the device as known by HP IMC. The device must be
                be supported in the HP IMC platform ICC module.
         ipmacarp: returns the current device maciparp table as discovered by HP IMC.

         The imc_dev class supports the following methods which can be called upon an instance of this class

         addvlan: This method executes the addvlan function on the specific instance of the imc_dev object. Devices must
                  supported in the HP IMC Platform VLAN Manager module.

         """

    def __init__(self, ip_address):
        self.ip = get_dev_details(ip_address)['ip']
        self.description = get_dev_details(ip_address)['sysDescription']
        self.location = get_dev_details(ip_address)['location']
        self.contact = get_dev_details(ip_address)['contact']
        self.type = get_dev_details(ip_address)['typeName']
        self.name = get_dev_details(ip_address)['sysName']
        self.status = get_dev_details(ip_address)['statusDesc']
        self.devid = get_dev_details(ip_address)['id']

        self.interfacelist = get_dev_interface(self.devid)
        self.numinterface = len(get_dev_interface(self.devid))
        self.vlans = get_dev_vlans(self.devid)['vlan']
        self.accessinterfaces = get_device_access_interfaces(self.devid)
        self.trunkinterfaces = get_trunk_interfaces(self.devid)
        self.alarm = get_dev_alarms(self.devid)
        self.numalarm = len(get_dev_alarms(self.devid))
        self.serials = get_serial_numbers(get_dev_asset_details(self.ip))
        self.assets = get_dev_asset_details(self.ip)
        self.runconfig = get_dev_run_config(self.devid)
        self.startconfig = get_dev_start_config(self.devid)
        self.ipmacarp = get_ip_mac_arp_list(self.devid)

    def addvlan(self, vlanid, vlan_name):
        create_dev_vlan(self.devid, vlanid, vlan_name)

    def delvlan(self, vlanid):
        delete_dev_vlans(self.devid, vlanid)


class IMCInterface:
    def __init__(self, ip_address, ifIndex):
        self.ip = get_dev_details(ip_address)['ip']
        self.devid = get_dev_details(ip_address)['id']
        self.ifIndex = get_interface_details(self.devid, ifIndex)['ifIndex']
        self.macaddress = get_interface_details(self.devid, ifIndex)['phyAddress']
        self.status = get_interface_details(self.devid, ifIndex)['statusDesc']
        self.adminstatus = get_interface_details(self.devid, ifIndex)['adminStatusDesc']
        self.name = get_interface_details(self.devid, ifIndex)['ifDescription']
        self.description = get_interface_details(self.devid, ifIndex)
        self.mtu = get_interface_details(self.devid, ifIndex)['mtu']
        self.speed = get_interface_details(self.devid, ifIndex)['ifspeed']
        self.accessinterfaces = get_device_access_interfaces(self.devid)
        self.pvid = get_access_interface_vlan(self.ifIndex, self.accessinterfaces)


class Host(IMCDev):
    def __init__(self, ip_address):
        self.hostip = get_real_time_locate(ip_address)['locateIp']
        self.deviceip = get_real_time_locate(ip_address)['deviceIp']
        self.ifIndex = get_real_time_locate(ip_address)['ifIndex']
        self.devid = get_real_time_locate(ip_address)['deviceId']
        self.accessinterfaces = get_device_access_interfaces(self.devid)
        self.pvid = get_access_interface_vlan(self.ifIndex, self.accessinterfaces)
        self.devstatus = get_dev_details(self.deviceip)['statusDesc']
        self.intstatus = get_interface_details(self.devid, self.ifIndex)['statusDesc']

    def down(self):
        set_inteface_down(self.devid, self.ifIndex)

    def up(self):
        set_inteface_up(self.devid, self.ifIndex)


class Hypervisor(IMCDev):
    def __init__(self, ipaddress):
        IMCDev.__init__(self, ipaddress)
        self.vmguests = get_host_vm_guest(self.devid)
        self.nics = get_host_vm_nic(self.devid)
        self.hostinfo = None


def get_dev_asset_details(ipaddress):
    """Takes in ipaddress as input to fetch device assett details from HP IMC RESTFUL API
    :param ipaddress: IP address of the device you wish to gather the asset details
    :return: object of type list containing the device asset details
    """
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_dev_asset_url = "/imcrs/netasset/asset?assetDevice.ip=" + str(ipaddress)
    f_url = url + get_dev_asset_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    if r.status_code == 200:
        dev_asset_info = (json.loads(r.text))
        if len(dev_asset_info) > 0:
            dev_asset_info = dev_asset_info['netAsset']
        if type(dev_asset_info) == dict:
            dev_asset_info = [dev_asset_info]
        if type(dev_asset_info) == list:
            dev_asset_info[:] = [dev for dev in dev_asset_info if dev.get('deviceIp') == ipaddress]
        return dev_asset_info
    else:
        print("get_dev_asset_details:  An Error has occured")


def get_serial_numbers(assetList):
    """
    Helper function: Uses return of get_dev_asset_details function to evaluate to evaluate for multipe serial objects.
    :param assetList: output of get_dev_asset_details function
    :return: the serial_list object of list type which contains one or more dictionaries of the asset details
    """
    serial_list = []
    if type(assetList) == list:
        for i in assetList:
            if len(i['serialNum']) > 0:
                serial_list.append(i)
    return serial_list


def get_trunk_interfaces(devId):
    """Function takes devId as input to RESTFULL call to HP IMC platform
    :param devId: output of get_dev_details
    :return: list of dictionaries containing of interfaces configured as an 802.1q trunk
    """

    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_trunk_interfaces_url = "/imcrs/vlan/trunk?devId=" + str(devId) + "&start=1&size=5000&total=false"
    f_url = url + get_trunk_interfaces_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    if r.status_code == 200:
        dev_trunk_interfaces = (json.loads(r.text))
        if len(dev_trunk_interfaces) == 2:
            return dev_trunk_interfaces['trunkIf']
        else:
            dev_trunk_interfaces['trunkIf'] = ["No trunk inteface"]
            return dev_trunk_interfaces['trunkIf']


def get_device_access_interfaces(devId):
    """Function takes devId as input to RESTFUL call to HP IMC platform
    :param devId: requires deviceID as the only input parameter
    :return: list of dictionaries containing interfaces configured as access ports
    """
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_access_interface_vlan_url = "/imcrs/vlan/access?devId=" + str(devId) + "&start=1&size=500&total=false"
    f_url = url + get_access_interface_vlan_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    if r.status_code == 200:
        dev_access_interfaces = (json.loads(r.text))
        if len(dev_access_interfaces) == 2:
            return dev_access_interfaces['accessIf']
        else:
            dev_access_interfaces['accessIf'] = ["No access inteface"]
            return dev_access_interfaces['accessIf']
    else:
        print("get_device_access_interfaces: An Error has occured")


def get_access_interface_vlan(ifIndex, accessinterfacelist):
    for i in accessinterfacelist:
        if i['ifIndex'] == ifIndex:
            return i['pvid']
        else:
            return "Not an Access Port"


def get_interface_details(devId, ifIndex):
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_interface_details_url = "/imcrs/plat/res/device/" + str(devId) + "/interface/" + str(ifIndex)
    f_url = url + get_interface_details_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    if r.status_code == 200:
        dev_details = (json.loads(r.text))
        return dev_details
    else:
        print("get_interface_details: An Error has occured")


def get_dev_details(ip_address):
    """Takes string input of IP address to issue RESTUL call to HP IMC
    :param ip_address: string object of dotted decimal notation of IPv4 address
    :return: dictionary of device details

    >>> get_dev_details('10.101.0.1')
    {'symbolLevel': '2', 'typeName': 'Cisco 2811', 'location': 'changed this too', 'status': '1', 'sysName': 'Cisco2811.haw.int', 'id': '30', 'symbolType': '3', 'symbolId': '1032', 'sysDescription': '', 'symbolName': 'Cisco2811.haw.int', 'mask': '255.255.255.0', 'label': 'Cisco2811.haw.int', 'symbolDesc': '', 'sysOid': '1.3.6.1.4.1.9.1.576', 'contact': 'changed this too', 'statusDesc': 'Normal', 'parentId': '1', 'categoryId': '0', 'topoIconName': 'iconroute', 'mac': '00:1b:d4:47:1e:68', 'devCategoryImgSrc': 'router', 'link': {'@rel': 'self', '@href': 'http://10.101.0.202:8080/imcrs/plat/res/device/30', '@op': 'GET'}, 'ip': '10.101.0.1'}
    
    >>> get_dev_details('8.8.8.8')
    Device not found
    'Device not found'
    """
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_dev_details_url = "/imcrs/plat/res/device?resPrivilegeFilter=false&ip=" + \
                          str(ip_address) + "&start=0&size=1000&orderBy=id&desc=false&total=false"
    f_url = url + get_dev_details_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    if r.status_code == 200:
        dev_details = (json.loads(r.text))
        if len(dev_details) == 0:
            print("Device not found")
            return "Device not found"
        elif type(dev_details['device']) == list:
            for i in dev_details['device']:
                if i['ip'] == ip_address:
                    dev_details = i
                    return dev_details
        elif type(dev_details['device']) == dict:
            return dev_details['device']
    else:
        print("dev_details: An Error has occured")


def get_dev_vlans(devId):
    """Function takes input of devID to issue RESTUL call to HP IMC
    :param devId: requires devId as the only input parameter
    :return: dictionary of existing vlans on the devices. Device must be supported in HP IMC platform VLAN manager module
    """

    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_dev_vlans_url = "/imcrs/vlan?devId=" + str(devId) + "&start=0&size=5000&total=false"
    f_url = url + get_dev_vlans_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    if r.status_code == 200:
        dev_details = (json.loads(r.text))
        return dev_details
    elif r.status_code == 409:
        return {'vlan': 'no vlans'}
    else:
        print("get_dev_vlans: An Error has occured")


def get_dev_interface(devid):
    """
    Function takes devid as input to RESTFUL call to HP IMC platform
    :param devid: requires devid as the only input
    :return: list object which contains a dictionary per interface
    """
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_dev_interface_url = "/imcrs/plat/res/device/" + str(devid) + \
                            "/interface?start=0&size=1000&desc=false&total=false"
    f_url = url + get_dev_interface_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    if r.status_code == 200:
        int_list = (json.loads(r.text))['interface']
        return int_list
    else:
        print("An Error has occured")


def get_dev_run_config(devId):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the most current running config
    file as known by the HP IMC Base Platform ICC module for the target device.
    :param devId:  int or str value of the target device
    :return: str which contains the entire content of the target device running configuration. If the device is not
    currently supported in the HP IMC Base Platform ICC module, this call returns a string of "This feature is not
    supported on this device"
    """
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_dev_run_url = "/imcrs/icc/deviceCfg/" + str(devId) + "/currentRun"
    f_url = url + get_dev_run_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # print (r.status_code)
    if r.status_code == 200:
        run_conf = (json.loads(r.text))['content']
        type(run_conf)
        if run_conf is None:
            return "This features is no supported on this device"
        else:
            return run_conf
    else:
        return "This features is not supported on this device"


def get_dev_start_config(devId):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the most current startup config
    file as known by the HP IMC Base Platform ICC module for the target device.
    :param devId:  int or str value of the target device
    :return: str which contains the entire content of the target device startup configuration. If the device is not
    currently supported in the HP IMC Base Platform ICC module, this call returns a string of "This feature is not
    supported on this device"
    """
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_dev_run_url = "/imcrs/icc/deviceCfg/" + str(devId) + "/currentStart"
    f_url = url + get_dev_run_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    if r.status_code == 200:
        start_conf = (json.loads(r.text))['content']
        return start_conf
    else:
        # print (r.status_code)
        return "This feature is not supported on this device"


def get_dev_alarms(devId):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the current alarms for the target
    device.
    :param devId: int or str value of the target device
    :return:list of dictionaries containing the alarms for this device
    """
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_dev_alarm_url = "/imcrs/fault/alarm?operatorName=admin&deviceId=" + \
                        str(devId) + "&desc=false"
    f_url = url + get_dev_alarm_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    if r.status_code == 200:
        dev_alarm = (json.loads(r.text))
        if 'alarm' in dev_alarm:
            return dev_alarm['alarm']
        else:
            return "Device has no alarms"

"""
This section deals with functions to access the HP IMC Base Platform Terminal Access Specific API calls
"""

def get_real_time_locate(ipAddress):
    """
    function takes the ipAddress of a specific host and issues a RESTFUL call to get the device and interface that the
    target host is currently connected to.
    :param ipAddress: str value valid IPv4 IP address
    :return: dictionary containing hostIp, devId, deviceIP, ifDesc, ifIndex
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    real_time_locate_url = "/imcrs/res/access/realtimeLocate?type=2&value=" + str(ipAddress) + "&total=false"
    f_url = url + real_time_locate_url
    r = requests.get(f_url, auth=auth, headers=headers)  # creates the URL using the payload variable as the contents
    if r.status_code == 200:
        return json.loads(r.text)['realtimeLocation']

    else:
        print(r.status_code)
        print("An Error has occured")


def get_ip_mac_arp_list(devId):
    """
    function takes devid of specific device and issues a RESTFUL call to get the IP/MAC/ARP list from the target device.
    :param devId: int or str value of the target device.
    :return: list of dictionaries containing the IP/MAC/ARP list of the target device.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    ip_mac_arp_list_url = "/imcrs/res/access/ipMacArp/" + str(devId)
    f_url = url + ip_mac_arp_list_url
    r = requests.get(f_url, auth=auth, headers=headers)  # creates the URL using the payload variable as the contents
    if r.status_code == 200:
        macarplist = (json.loads(r.text))
        if len(macarplist) > 1:
            return macarplist['ipMacArp']
        else:
            return 'this function is unsupported'

    else:
        print(r.status_code)
        print("An Error has occured")


"""
This section contains functions to work with the various custom views available within HPE IMC Base Platform
"""

def get_custom_views(name=None):
    """
    function takes no input and issues a RESTFUL call to get a list of custom views from HPE IMC. Optioanl Name input
    will return only the specified view.
    :param name: string containg the name of the desired custom view
    :return: list of dictionaries containing attributes of the custom views.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    if name is None:
        get_custom_views_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&desc=false&total=false'
    elif name is not None:
        get_custom_views_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&name='+ name + '&desc=false&total=false'
    f_url = url + get_custom_views_url
    r = requests.get(f_url, auth=auth, headers=headers)  # creates the URL using the payload variable as the contents
    if r.status_code == 200:
        customviewlist = (json.loads(r.text))['customView']
        if type(customviewlist) is dict:
            customviewlist = [customviewlist]
            return customviewlist
        else:
            return customviewlist
    else:
        print(r.status_code)
        print("An Error has occured")

def create_custom_views(name=None, upperview=None):
    """
    function takes no input and issues a RESTFUL call to get a list of custom views from HPE IMC. Optioanl Name input
    will return only the specified view.
    :param name: string containg the name of the desired custom view
    :return: list of dictionaries containing attributes of the custom views.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    create_custom_views_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&desc=false&total=falsee'
    f_url = url + create_custom_views_url
    if upperview is None:
        payload = '''{ "name": "''' + name + '''",
         "upLevelSymbolId" : ""}'''
    else:
        parentviewid = get_custom_views(upperview)[0]['symbolId']
        payload = '''{
                         "name": "'''+name+ '''"upperview" : "'''+str(parentviewid)+'''"}'''
        print (payload)
    r = requests.post(f_url, data = payload, auth=auth, headers=headers)  # creates the URL using the payload variable as the contents
    if r.status_code == 201:
        return 'View ' + name +' created successfully'
    else:
        print(r.status_code)
        print("An Error has occured")
"""
This section contains functions which access the HP IMC Base Platform VLAN Manager specific API calls
 """

def create_dev_vlan(devid, vlanid, vlan_name):
    """
    function takes devid and vlanid vlan_name of specific device and 802.1q VLAN tag and issues a RESTFUL call to add the
    specified VLAN from the target device. VLAN Name MUST be valid on target device.
    :param devid: int or str value of the target device
    :param vlanid:int or str value of target 802.1q VLAN
    :param vlan_name: str value of the target 802.1q VLAN name. MUST be valid name on target device.
    :return:HTTP Status code of 204 with no values.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    create_dev_vlan_url = "/imcrs/vlan?devId=" + str(devid)
    f_url = url + create_dev_vlan_url
    payload = '''{ "vlanId": "''' + str(vlanid) + '''", "vlanName" : "''' + str(vlan_name) + '''"}'''
    r = requests.post(f_url, data=payload, auth=auth,
                      headers=headers)  # creates the URL using the payload variable as the contents
    print(r.status_code)
    if r.status_code == 201:
        return r.status_code
    else:
        print("An Error has occured")


def delete_dev_vlans(devid, vlanid):
    """
    function takes devid and vlanid of specific device and 802.1q VLAN tag and issues a RESTFUL call to remove the
    specified VLAN from the target device.
    :param devid: int or str value of the target device
    :param vlanid:
    :return:HTTP Status code of 204 with no values.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    remove_dev_vlan_url = "/imcrs/vlan/delvlan?devId=" + str(devid) + "&vlanId=" + str(vlanid)
    f_url = url + remove_dev_vlan_url
    payload = None
    r = requests.delete(f_url, auth=auth,
                        headers=headers)  # creates the URL using the payload variable as the contents
    print(r.status_code)
    if r.status_code == 204:
        return r.status_code
    else:
        print("An Error has occured")

"""
This section deals with functions which access the HP IMC Base Platform Device Resource specific API calls.
"""

def set_inteface_down(devid, ifindex):
    """
    function takest devid and ifindex of specific device and interface and issues a RESTFUL call to " shut" the specifie
    d interface on the target device.
    :param devid: int or str value of the target device
    :param ifindex: int or str value of the target interface
    :return: HTTP status code 204 with no values.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    set_int_down_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + str(ifindex) + "/down"
    f_url = url + set_int_down_url
    payload = None
    r = requests.put(f_url, auth=auth,
                     headers=headers)  # creates the URL using the payload variable as the contents
    print(r.status_code)
    if r.status_code == 204:
        return r.status_code
    else:
        print("An Error has occured")


def set_inteface_up(devid, ifindex):
    """
    function takest devid and ifindex of specific device and interface and issues a RESTFUL call to "undo shut" the spec
    ified interface on the target device.
    :param devid: int or str value of the target device
    :param ifindex: int or str value of the target interface
    :return: HTTP status code 204 with no values.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    set_int_up_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + str(ifindex) + "/up"
    f_url = url + set_int_up_url
    payload = None
    r = requests.put(f_url, auth=auth,
                     headers=headers)  # creates the URL using the payload variable as the contents
    print(r.status_code)
    if r.status_code == 204:
        return r.status_code
    else:
        print("An Error has occured")


def get_vm_host_info(hostId):
    """
    function takes hostId as input to RESTFUL call to HP IMC
    :param hostId: int or string of HostId of Hypervisor host
    :return:list of dictionatires contraining the VM Host information for the target hypervisor
    """
    global r
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    get_vm_host_info_url = "/imcrs/vrm/host?hostId=" + str(hostId)
    f_url = url + get_vm_host_info_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=headers)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    if r.status_code == 200:
        if len(r.text) > 0:
            return json.loads(r.text)
    elif r.status_code == 204:
        print("Device is not a supported Hypervisor")
        return "Device is not a supported Hypervisor"
    else:
        print("An Error has occured")


def get_host_info(hostId):
    """
    function takes hostId as input to RESTFUL call to HP IMC
    :param hostId: int or string of HostId of Hypervisor host
    :return: list of dictionaries containing the host information for the target hypervisor
    """
    global r
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    get_host_info_url = "/imcrs/vrm/host/vm?hostId=" + str(hostId)
    f_url = url + get_host_info_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=headers)  # creates the URL using the payload variable as the contents
    print(r.status_code)
    if r.status_code == 200:
        if len(json.loads(r.text)) > 1:
            return json.loads(r.text)['vmDevice']
        else:
            return "Device is not a supported Hypervisor"
    else:
        print(r.text)
        print("An Error has occured")


def get_host_vm_guest(hostId):
    """
    function takes hostId as input to RESTFUL call to HP IMC
    :param hostId: HostId of Hypervisor host.
    :return: list of dictionaries containing the VM Guest information for the target hypervisor
    """
    global r
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    get_host_vm_guest_url = "/imcrs/vrm/host/vm?hostId=" + str(hostId)
    f_url = url + get_host_vm_guest_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=headers)  # creates the URL using the payload variable as the contents
    print(r.status_code)
    if r.status_code == 200:
        if len(r.text) > 0:
            return json.loads(r.text)['vmDevice']
    else:
        print(r.text)
        print("An Error has occured")


def get_host_vm_nic(hostId):
    """
    function takes hostId as input to RESTFUL call to HP IMC
    :param hostId: hostID of Hypervisor host.
    :return: list of dictionaries containing the NIC information for the target hypervisor
    """
    global r
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    get_host_vm_nic_url = "/imcrs/vrm/host/vnic?hostDevId=" + str(hostId)
    f_url = url + get_host_vm_nic_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=headers)  # creates the URL using the payload variable as the contents
    print(r.status_code)
    if r.status_code == 200:
        if len(r.text) > 0:
            return json.loads(r.text)['Nic']
    else:
        print(r.text)
        print("An Error has occured")
"""
System Level Functions
"""


def get_trap_definitions():
    """Takes in no param as input to fetch SNMP TRAP definitions from HP IMC RESTFUL API
    :param None
    :return: object of type list containing the device asset details
    """
    # checks to see if the imc credentials are already available
    if auth is None or url is None:
        set_imc_creds()
    global r
    get_trap_def_url = "/imcrs/fault/trapDefine/sync/query?enterpriseId=1.3.6.1.4.1.11&size=10000"
    f_url = url + get_trap_def_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    # r.status_code
    if r.status_code == 200:
        trap_def_list = (json.loads(r.text))
        return trap_def_list['trapDefine']
    else:
        print("get_dev_asset_details:  An Error has occured")



"""
next section specifies the HP IMC authentication handler
"""

# url header to preprend on all IMC eAPI calls
url = None

# auth handler for eAPI calls
auth = None

# headers forcing IMC to respond with JSON content. XML content return is
# the default
headers = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}





"""========================
Helper Functions
==========================="""

def print_to_file(object):
    '''
    Function takes in object of type str, list, or dict and prints out to current working directory as pyoutput.txt
    :param:  Object: object of type str, list, or dict
    :return: No return. Just prints out to file handler and save to current working directory as pyoutput.txt
    '''
    with open ('pyoutput.txt', 'w') as fh:
        x = None
        if type(object) is list:
            x = json.dumps(object, indent = 4)
        if type(object) is dict:
            x = json.dumps(object, indent = 4)
        if type (object) is str:
            x = object
        fh.write(x)

def print_to_csv(list_of_dicts):
    with open('file.csv', 'w') as output:
        w = csv.DictWriter(output, list_of_dicts[0].keys())
        w = w.writeheader()
        w = w.writerows(list_of_dicts)






def set_imc_creds():
    """ This function prompts user for IMC server information and credentuials and stores
    values in url and auth global variables"""
    global url, auth, r
    imc_protocol = input(
        "What protocol would you like to use to connect to the IMC server: \n Press 1 for HTTP: \n Press 2 for HTTPS:")
    if imc_protocol == "1":
        h_url = 'http://'
    else:
        h_url = 'https://'
    imc_server = input("What is the ip address of the IMC server?")
    imc_port = input("What is the port number of the IMC server?")
    imc_user = input("What is the username of the IMC eAPI user?")
    imc_pw = input('''What is the password of the IMC eAPI user?''')
    url = h_url + imc_server + ":" + imc_port
    auth = requests.auth.HTTPDigestAuth(imc_user, imc_pw)
    test_url = '/imcrs'
    f_url = url + test_url
    try:
        r = requests.get(f_url, auth=auth, headers=headers, verify=False)
    # checks for reqeusts exceptions
    except requests.exceptions.RequestException as e:
        print("Error:\n" + str(e))
        print("\n\nThe IMC server address is invalid. Please try again\n\n")
        set_imc_creds()
    if r.status_code != 200:  # checks for valid IMC credentials
        print("Error: \n You're credentials are invalid. Please try again\n\n")
        set_imc_creds()
    else:
        print("You've successfully access the IMC eAPI")

