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


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

#command creates dummy IMCAuth object. Should be overwritten in script calling these functions



"""
This section contains functions which operate at the device level
"""
def get_dev_vlans(devid, auth, url):
    """Function takes input of devID to issue RESTUL call to HP IMC
    :param devid: requires devId as the only input parameter
    :return: dictionary of existing vlans on the devices. Device must be supported in HP IMC platform VLAN manager module
    """

    # checks to see if the imc credentials are already available
    get_dev_vlans_url = "/imcrs/vlan?devId=" + str(devid) + "&start=0&size=5000&total=false"
    f_url = url + get_dev_vlans_url

    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_vlans = (json.loads(r.text))
            return dev_vlans['vlan']
        elif r.status_code == 409:
            return {'vlan': 'no vlans'}
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_dev_vlans: An Error has occured'

def get_trunk_interfaces(devId, auth, url):
    """Function takes devId as input to RESTFULL call to HP IMC platform
    :param devId: output of get_dev_details
    :return: list of dictionaries containing of interfaces configured as an 802.1q trunk

    Example:
        auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")
        get_dev_asset_details("2", auth.creds, auth.url)
    """

    # checks to see if the imc credentials are already available
    get_trunk_interfaces_url = "/imcrs/vlan/trunk?devId=" + str(devId) + "&start=1&size=5000&total=false"
    f_url = url + get_trunk_interfaces_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_trunk_interfaces = (json.loads(r.text))
        if len(dev_trunk_interfaces) == 2:
            return dev_trunk_interfaces['trunkIf']
        else:
            dev_trunk_interfaces['trunkIf'] = ["No trunk inteface"]
            return dev_trunk_interfaces['trunkIf']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' get_trunk_interfaces: An Error has occured'




def get_device_access_interfaces(devId, auth, url):
    """Function takes devId as input to RESTFUL call to HP IMC platform
    :param devId: requires deviceID as the only input parameter
    :return: list of dictionaries containing interfaces configured as access ports
    """
    # checks to see if the imc credentials are already available
    get_access_interface_vlan_url = "/imcrs/vlan/access?devId=" + str(devId) + "&start=1&size=500&total=false"
    f_url = url + get_access_interface_vlan_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_access_interfaces = (json.loads(r.text))
            if len(dev_access_interfaces) == 2:
                return dev_access_interfaces['accessIf']
            else:
                dev_access_interfaces['accessIf'] = ["No access inteface"]
                return dev_access_interfaces['accessIf']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_device_access_interfaces: An Error has occured"


def get_access_interface_vlan(ifIndex, accessinterfacelist, auth, url):
    for i in accessinterfacelist:
        if i['ifIndex'] == ifIndex:
            return i['pvid']
        else:
            return "Not an Access Port"



def create_dev_vlan(devid, vlanid, vlan_name, auth, url):
    """
    function takes devid and vlanid vlan_name of specific device and 802.1q VLAN tag and issues a RESTFUL call to add the
    specified VLAN from the target device. VLAN Name MUST be valid on target device.
    :param devid: int or str value of the target device
    :param vlanid:int or str value of target 802.1q VLAN
    :param vlan_name: str value of the target 802.1q VLAN name. MUST be valid name on target device.
    :return:HTTP Status code of 201 with no values.
    """
    create_dev_vlan_url = "/imcrs/vlan?devId=" + str(devid)
    f_url = url + create_dev_vlan_url
    payload = '''{ "vlanId": "''' + str(vlanid) + '''", "vlanName" : "''' + str(vlan_name) + '''"}'''
    r = requests.post(f_url, data=payload, auth=auth,
                      headers=HEADERS)  # creates the URL using the payload variable as the contents
    return r
    try:

        if r.status_code == 201:
            print ('Vlan Created')
            return r.status_code
        elif r.status_code == 409:
            return '''Unable to create VLAN.\nVLAN Already Exists\nDevice does not support VLAN function'''
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " create_dev_vlan: An Error has occured"


def delete_dev_vlans(devid, vlanid, auth, url):
    """
    function takes devid and vlanid of specific device and 802.1q VLAN tag and issues a RESTFUL call to remove the
    specified VLAN from the target device.
    :param devid: int or str value of the target device
    :param vlanid:
    :return:HTTP Status code of 204 with no values.
    """
    remove_dev_vlan_url = "/imcrs/vlan/delvlan?devId=" + str(devid) + "&vlanId=" + str(vlanid)
    f_url = url + remove_dev_vlan_url
    payload = None
    r = requests.delete(f_url, auth=auth,
                        headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 204:
            print ('Vlan deleted')
            return r.status_code
        elif r.status_code == 409:
            print ('Unable to delete VLAN.\nVLAN does not Exist\nDevice does not support VLAN function')
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " delete_dev_vlans: An Error has occured"




"""
This section contains functions which operate at the interface level
"""