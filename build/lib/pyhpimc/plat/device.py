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
import json
import requests


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

#auth = None


"""
This section contains functions which operate at the device level
"""
def get_dev_details(ip_address, auth, url):
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
    get_dev_details_url = "/imcrs/plat/res/device?resPrivilegeFilter=false&ip=" + \
                          str(ip_address) + "&start=0&size=1000&orderBy=id&desc=false&total=false"
    f_url = url + get_dev_details_url
        # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
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
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_details: An Error has occured"


def get_dev_interface(devid, auth, url):
    """
    Function takes devid as input to RESTFUL call to HP IMC platform
    :param devid: requires devid as the only input
    :return: list object which contains a dictionary per interface
    """
    # checks to see if the imc credentials are already available
    get_dev_interface_url = "/imcrs/plat/res/device/" + str(devid) + \
                            "/interface?start=0&size=1000&desc=false&total=false"
    f_url = url + get_dev_interface_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            int_list = (json.loads(r.text))['interface']
            return int_list
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_interface: An Error has occured"


def get_dev_run_config(devid, auth, url):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the most current running config
    file as known by the HP IMC Base Platform ICC module for the target device.
    :param devid:  int or str value of the target device
    :return: str which contains the entire content of the target device running configuration. If the device is not
    currently supported in the HP IMC Base Platform ICC module, this call returns a string of "This feature is not
    supported on this device"
    """
    # checks to see if the imc credentials are already available
    get_dev_run_url = "/imcrs/icc/deviceCfg/" + str(devid) + "/currentRun"
    f_url = url + get_dev_run_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # print (r.status_code)
    try:
        if r.status_code == 200:
            try:
                run_conf = (json.loads(r.text))['content']
                return run_conf
            except:
                return "This features is no supported on this device"
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_run_config: An Error has occured"


def get_dev_start_config(devId, auth, url):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the most current startup config
    file as known by the HP IMC Base Platform ICC module for the target device.
    :param devId:  int or str value of the target device
    :return: str which contains the entire content of the target device startup configuration. If the device is not
    currently supported in the HP IMC Base Platform ICC module, this call returns a string of "This feature is not
    supported on this device"
    """
    # checks to see if the imc credentials are already available
    get_dev_run_url = "/imcrs/icc/deviceCfg/" + str(devId) + "/currentStart"
    f_url = url + get_dev_run_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if r.status_code == 200:
            try:
                start_conf = (json.loads(r.text))['content']
                return start_conf
            except:
                return "Start Conf not supported on this device"

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_dev_run_config: An Error has occured"




"""
This section contains functions which operate at the interface level
"""

def get_interface_details(devId, ifIndex, auth, url):
    # checks to see if the imc credentials are already available
    get_interface_details_url = "/imcrs/plat/res/device/" + str(devId) + "/interface/" + str(ifIndex)
    f_url = url + get_interface_details_url
    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    try:
        if r.status_code == 200:
            dev_details = (json.loads(r.text))
            return dev_details
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_interface_details: An Error has occured"



def set_inteface_down(devid, ifindex, auth, url):
    """
    function takest devid and ifindex of specific device and interface and issues a RESTFUL call to " shut" the specifie
    d interface on the target device.
    :param devid: int or str value of the target device
    :param ifindex: int or str value of the target interface
    :return: HTTP status code 204 with no values.
    """
    set_int_down_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + str(ifindex) + "/down"
    f_url = url + set_int_down_url
    try:
        r = requests.put(f_url, auth=auth,
                         headers=HEADERS)  # creates the URL using the payload variable as the contents
        print(r.status_code)
        if r.status_code == 204:
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " set_inteface_down: An Error has occured"


def set_inteface_up(devid, ifindex, auth, url):
    """
    function takest devid and ifindex of specific device and interface and issues a RESTFUL call to "undo shut" the spec
    ified interface on the target device.
    :param devid: int or str value of the target device
    :param ifindex: int or str value of the target interface
    :return: HTTP status code 204 with no values.
    """
    set_int_up_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + str(ifindex) + "/up"
    f_url = url + set_int_up_url
    try:
        r = requests.put(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
        if r.status_code == 204:
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " set_inteface_up: An Error has occured"
