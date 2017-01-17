#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the device capabilities
of the HPE IMC NMS platform using the RESTful API

"""

# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS


# This section contains functions which operate at the system level
# This whole section has been moved to pyhpeimc.plat.system - functions left here for legacy.
# Intention is to remove by version 1.0.60 or greater. Please modify any scripts using functions
# in this section to use the new functions in the new module



# TODO Delete function when version => 1.60
def get_system_vendors(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single vendor

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> vendors = get_system_vendors(auth.creds, auth.url)

      >>> assert type(vendors) is list

      >>> assert 'name' in vendors[0]

    """
    f_url = url + '/imcrs/plat/res/vendor?start=0&size=10000&orderBy=id&desc=false&total=false'
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            system_vendors = (json.loads(response.text))
            return system_vendors['deviceVendor']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_details: An Error has occured"


# TODO remove function when version => 1.60
def get_system_category(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device category

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> categories = get_system_category(auth.creds, auth.url)

      >>> assert type(categories) is list

      >>> assert 'name' in categories[0]


    """
    f_url = url + '/imcrs/plat/res/category?start=0&size=10000&orderBy=id&desc=false&total=false'
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            system_category = (json.loads(response.text))
            return system_category['deviceCategory']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_details: An Error has occured"


# TODO Delete function when version => 1.60
def get_system_device_models(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device model

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> device_models = get_system_device_models(auth.creds, auth.url)

      >>> assert type(device_models) is list

      >>> assert 'virtualDeviceName' in device_models[0]

    """
    f_url = url + '/imcrs/plat/res/model?start=0&size=10000&orderBy=id&desc=false&total=false'
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            system_device_model = (json.loads(response.text))
            return system_device_model['deviceModel']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_details: An Error has occured"


# TODO Delete function when version => 1.60
def get_system_series(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device series

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> series = get_system_series(auth.creds, auth.url)

      >>> assert type(series) is list

      >>> assert 'name' in series[0]

    """
    f_url = url + '/imcrs/plat/res/series?managedOnly=false&start=0&size=10000&orderBy=id&desc' \
                   '=false&total=false'
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            system_series = (json.loads(response.text))
            return system_series['deviceSeries']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_series: An Error has occured"


# This section contains functions which operate at the device level.


def get_all_devs(auth, url, network_address=None):
    """Takes string input of IP address to issue RESTUL call to HP IMC\n

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param network_address= str IPv4 Network Address

    :return: dictionary of device details

    :rtype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> dev_list = get_all_devs( auth.creds, auth.url, network_address= '10.11.')

    >>> assert type(dev_list) is list

    >>> assert 'sysName' in dev_list[0]

    """
    if network_address is not None:
        get_all_devs_url = "/imcrs/plat/res/device?resPrivilegeFilter=false&ip=" + \
                           str(network_address) + \
                           "&start=0&size=1000&orderBy=id&desc=false&total=false"
    else:
        get_all_devs_url = ("/imcrs/plat/res/device?resPrivilegeFilter=false&start=0"
                            "&size=1000&orderBy=id&desc=false&total=false&exact=false")

    f_url = url + get_all_devs_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_details = (json.loads(response.text))
            if len(dev_details) == 0:
                print("Device not found")
                return "Device not found"
            else:
                return dev_details['device']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_details: An Error has occured"


def get_dev_details(ip_address, auth, url):
    """Takes string input of IP address to issue RESTUL call to HP IMC

    :param ip_address: string object of dotted decimal notation of IPv4 address

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: dictionary of device details

    :rtype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> dev_1 =  get_dev_details('10.101.0.221', auth.creds, auth.url)

    >>> assert type(dev_1) is dict

    >>> assert 'sysName' in dev_1

    >>> dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
    Device not found

    >>> assert type(dev_2) is str

    """
    get_dev_details_url = "/imcrs/plat/res/device?resPrivilegeFilter=false&ip=" + \
                          str(ip_address) + "&start=0&size=1000&orderBy=id&desc=false&total=false"
    f_url = url + get_dev_details_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_details = (json.loads(response.text))
            if len(dev_details) == 0:
                print("Device not found")
                return "Device not found"
            elif isinstance(dev_details['device'], list):
                for i in dev_details['device']:
                    if i['ip'] == ip_address:
                        dev_details = i
                        return dev_details
            elif isinstance(dev_details['device'], dict):
                return dev_details['device']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_details: An Error has occured"


def get_dev_interface(auth, url, devid=None, devip=None):
    """
    Function takes devid as input to RESTFUL call to HP IMC platform and returns list of device
    interfaces

    :param devid: optional devid as the input

    :param devip: str of ipv4 address of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass


    :return: list object which contains a dictionary per interface

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> dev_interfaces = get_dev_interface(auth.creds, auth.url, devid='15')

    >>> dev_interfaces = get_dev_interface(auth.creds, auth.url, devip='10.101.0.221')

    >>> assert type(dev_interfaces) is list

    >>> assert 'ifAlias' in dev_interfaces[0]

   """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    get_dev_interface_url = "/imcrs/plat/res/device/" + str(devid) + \
                            "/interface?start=0&size=1000&desc=false&total=false"
    f_url = url + get_dev_interface_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            int_list = json.loads(response.text)
            if 'interface' in int_list:
                return int_list['interface']
            else:
                return []
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_interface: An Error has occured"


def get_dev_run_config(auth, url, devid=None, devip=None):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the most
    current  running config file as known by the HP IMC Base Platform ICC module for the target
    device.

    :param devid:  int or str value of the target device

    :param devip: str of ipv4 address of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str which contains the entire content of the target device running configuration.
    If the device is not currently supported in the HP IMC Base Platform ICC module, this call
    returns a string of "This feature is not supported on this device"

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> run_config = get_dev_run_config(auth.creds, auth.url, devid='10')

    >>> run_config = get_dev_run_config(auth.creds, auth.url, devip='10.101.0.221')

    >>> assert type(run_config) is str

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    f_url = url + "/imcrs/icc/deviceCfg/" + str(devid) + "/currentRun"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            run_conf = (json.loads(response.text))['content']
            return run_conf
        elif response.status_code == 404:
            return "This features is no supported on this device"
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_run_config: An Error has occured"


def get_dev_start_config(auth, url, devid=None, devip=None):
    """
    function takes the devId of a specific device and issues a RESTFUL call to get the most
    current startup config  file as known by the HP IMC Base Platform ICC module for the target
    device.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid:  optional int or str value of the target device

    :param devip:  optional ipv4 address of the target device

    :return: str which contains the entire content of the target device startup configuration.
    If the device is not currently supported in the HP IMC Base Platform ICC module, this call
    returns a string of "This feature is not supported on this device"

    :retype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> start_config = get_dev_start_config(auth.creds, auth.url, devId='10')

    >>> start_config = get_dev_start_config(auth.creds, auth.url, devip='10.101.0.221')

    >>> assert type(start_config) is str

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    f_url = url + "/imcrs/icc/deviceCfg/" + str(devid) + "/currentStart"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            start_conf = (json.loads(response.text))['content']
            return start_conf
        elif response.status_code == 404:
            return "This features is no supported on this device"
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_start_config: An Error has occured"


def get_dev_mac_learn(auth, url, devid=None, devip=None):
    """
    function takes devid of specific device and issues a RESTFUL call to gather the current
    IP-MAC  learning entries on the target device.

    :param devid: int value of the target device

    :param devip: ipv4 address of the target device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dict objects which contain the mac learn table of target device id

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> dev_mac_learn = get_dev_mac_learn( auth.creds, auth.url, devid='10')

    >>> dev_mac_learn = get_dev_mac_learn( auth.creds, auth.url, devip='10.101.0.221')

    >>> assert type(dev_mac_learn) is list

    >>> assert 'deviceId' in dev_mac_learn[0]

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    f_url = url + '/imcrs/res/access/ipMacLearn/' + str(devid)
    try:
        response = requests.get(f_url, auth=auth, headers=HEADERS)
        if response.status_code == 200:
            if len(json.loads(response.text)) < 1:
                mac_learn_query = []
                return mac_learn_query
            else:
                mac_learn_query = (json.loads(response.text))['ipMacLearnResult']
                if isinstance(mac_learn_query, dict):
                    mac_learn_query = [mac_learn_query]
                return mac_learn_query
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_mac_learn: An Error has occured"


def run_dev_cmd(cmd_list, auth, url, devid=None, devip=None):
    """
    Function takes devid of target device and a sequential list of strings which define the
    specific commands to be run on the target device and returns a str object containing the
    output of the commands.

    :param devid: int devid of the target device

    :param cmd_list: list of strings

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devip: str of ipv4 address of the target device

    :return: str containing the response of the commands

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> cmd_list = ['display version']

    >>> cmd_output = run_dev_cmd( cmd_list, auth.creds, auth.url, devid ='10')

    >>> cmd_output = run_dev_cmd( cmd_list, auth.creds, auth.url, devip='10.101.0.221')

    >>> assert type(cmd_output) is dict

    >>> assert 'cmdlist' in cmd_output

    >>> assert 'success' in cmd_output

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    run_dev_cmd_url = '/imcrs/icc/confFile/executeCmd'
    f_url = url + run_dev_cmd_url
    cmd_list = _make_cmd_list(cmd_list)
    payload = '''{ "deviceId" : "''' + str(devid) + '''",
                   "cmdlist" : { "cmd" :
                   [''' + cmd_list + ''']
                   }
                   }'''
    try:
        response = requests.post(f_url, data=payload, auth=auth, headers=HEADERS)
        if response.status_code == 200:
            if len(response.text) < 1:
                return ''
            else:
                return json.loads(response.text)
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " run_dev_cmd: An Error has occured"


# This section contains functions which operate at the interface level


def get_all_interface_details(auth, url, devid=None, devip=None):
    """
    function takes the devId of a specific device and the ifindex value assigned to a specific
    interface and issues a RESTFUL call to get the interface details file as known by the HP IMC
    Base Platform ICC module for the target device.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid:  int or str value of the devId of the target device

    :param devip: ipv4 address of the target device

    :return: list of dict objects which contains the details of all interfaces on the target device

    :retype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> all_interface_details = get_all_interface_details( auth.creds, auth.url, devId='10')

    >>> all_interface_details = get_all_interface_details( auth.creds, auth.url,
                                                           devip='10.101.0.221')

    >>> assert type(all_interface_details) is list

    >>> assert 'ifAlias' in all_interface_details[0]

     """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    get_all_interface_details_url = "/imcrs/plat/res/device/" + str(
        devid) + "/interface/?start=0&size=1000&desc=false&total=false"
    f_url = url + get_all_interface_details_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_details = (json.loads(response.text))
            return dev_details['interface']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_all_interface_details: An Error has occured"


def get_interface_details(ifindex, auth, url, devid=None, devip=None):
    """
    function takes the devId of a specific device and the ifindex value assigned to a specific
    interface  and issues a RESTFUL call to get the interface details
    file as known by the HP IMC Base Platform ICC module for the target device.

    :param ifindex: int or str value of the ifIndex of the target interface

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid:  int or str value of the devId of the target device

    :param devip: str of ipv4 address of the target device

    :return: dict which contains the details of the target interface"

    :retype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> interface_details = get_interface_details('1', auth.creds, auth.url, devId = '10')

    >>> interface_details = get_interface_details('1', auth.creds, auth.url, devip = '10.101.0.221')

    >>> assert type(interface_details) is dict

    >>> assert 'ifAlias' in interface_details

     """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    get_interface_details_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + \
                                str(ifindex)
    f_url = url + get_interface_details_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_details = (json.loads(response.text))
            return dev_details
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_interface_details: An Error has occured"


def set_interface_down(ifindex, auth, url, devid=None, devip=None):
    """
    function takest devid and ifindex of specific device and interface and issues a RESTFUL call
    to " shut" the specified interface on the target device.
    :param devid: int or str value of the target device

    :param devip: ipv4 address of the target devices

    :param ifindex: int or str value of the target interface

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: HTTP status code 204 with no values.

    :rtype:int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> int_up_response = set_inteface_up('9', auth.creds, auth.url, devip = '10.101.0.221')

    >>> int_down_response = set_interface_down( '9', auth.creds, auth.url, devid = '10')
    204

    >>> int_up_response = set_inteface_up('9', auth.creds, auth.url, devip = '10.101.0.221')

    >>> int_down_response = set_interface_down( '9', auth.creds, auth.url, devip = '10.101.0.221')
    204

    >>> assert type(int_down_response) is int

    >>> assert int_down_response is 204

    >>> int_up_response = set_inteface_up('9', auth.creds, auth.url, devip = '10.101.0.221')
    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    set_int_down_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + str(ifindex) + \
                       "/down"
    f_url = url + set_int_down_url
    try:
        response = requests.put(f_url, auth=auth, headers=HEADERS)
        print(response.status_code)
        if response.status_code == 204:
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " set_inteface_down: An Error has occured"


def set_inteface_up(ifindex, auth, url, devid=None, devip=None):
    """
    function takest devid and ifindex of specific device and interface and issues a RESTFUL call
    to "undo shut" the specified interface on the target device.

    :param devid: int or str value of the target device

    :param devip: ipv4 address of the target devices

    :param ifindex: int or str value of the target interface

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: HTTP status code 204 with no values.

    :rype: int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.device import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> int_down_response = set_interface_down( '9', auth.creds, auth.url, devid = '10')
    204

    >>> int_up_response = set_inteface_up( '9', auth.creds, auth.url, devid = '10')

    >>> int_down_response = set_interface_down( '9', auth.creds, auth.url, devid = '10')
    204

    >>> int_up_response = set_inteface_up('9', auth.creds, auth.url, devip = '10.101.0.221')

    >>> assert type(int_up_response) is int

    >>> assert int_up_response is 204

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    set_int_up_url = "/imcrs/plat/res/device/" + str(devid) + "/interface/" + str(ifindex) + "/up"
    f_url = url + set_int_up_url
    try:
        response = requests.put(f_url, auth=auth, headers=HEADERS)
        if response.status_code == 204:
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " set_inteface_up: An Error has occured"


def _make_cmd_list(cmd_list):
    """
    Helper function to easily create the proper json formated string from a list of strs
    :param cmd_list: list of strings
    :return: str json formatted
    """
    cmd = ''
    for i in cmd_list:
        cmd = cmd + '"' + i + '",'
    cmd = cmd[:-1]
    return cmd
