#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the VLAN Manager capabilities
of the HPE IMC NMS platform using the RESTful API

"""

# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS
from pyhpeimc.plat.device import get_dev_details

#pylint: disable=R0913
# This section contains functions which operate at the device level


def get_dev_vlans(auth, url, devid=None, devip=None):
    """Function takes input of devID to issue RESTUL call to HP IMC

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid: str requires devId as the only input parameter

    :param devip: str of ipv4 address of the target device

    :return: list of dictionaries where each element of the list represents one vlan on the
    target device

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> vlans = get_dev_vlans('350', auth.creds, auth.url)

    >>> assert type(vlans) is list

    >>> assert 'vlanId' in vlans[0]

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    get_dev_vlans_url = "/imcrs/vlan?devId=" + str(devid) + "&start=0&size=5000&total=false"
    f_url = url + get_dev_vlans_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_vlans = (json.loads(response.text))
            return dev_vlans['vlan']
        elif response.status_code == 409:
            return {'vlan': 'no vlans'}
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_dev_vlans: An Error has occured'


def get_trunk_interfaces(auth, url, devid=None, devip=None):
    """Function takes devId as input to RESTFULL call to HP IMC platform

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid: str requires devid of the target device

    :param devip: str of ipv4 address of the target device

    :return: list of dictionaries where each element of the list represents an interface which
    has been configured as a
    VLAN trunk port

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> trunk_interfaces = get_trunk_interfaces('10', auth.creds, auth.url)

    >>> assert type(trunk_interfaces) is list

    >>> assert len(trunk_interfaces[0]) == 3

    >>> assert 'allowedVlans' in trunk_interfaces[0]

    >>> assert 'ifIndex' in trunk_interfaces[0]

    >>> assert 'pvid' in trunk_interfaces[0]

    >>> get_trunk_interfaces('350', auth.creds, auth.url)
    ['No trunk inteface']
    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    get_trunk_interfaces_url = "/imcrs/vlan/trunk?devId=" + str(devid) + \
                               "&start=1&size=5000&total=false"
    f_url = url + get_trunk_interfaces_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_trunk_interfaces = (json.loads(response.text))
            if len(dev_trunk_interfaces) == 2:
                if isinstance(dev_trunk_interfaces['trunkIf'], list):
                    return dev_trunk_interfaces['trunkIf']
                elif isinstance(dev_trunk_interfaces['trunkIf'], dict):
                    return [dev_trunk_interfaces['trunkIf']]
            else:
                dev_trunk_interfaces['trunkIf'] = ["No trunk inteface"]
                return dev_trunk_interfaces['trunkIf']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_trunk_interfaces: An Error has occured'


def get_device_access_interfaces(auth, url, devid=None, devip=None):
    """
    Function takes devid pr devip as input to RESTFUL call to HP IMC platform

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid: str requires devid of the target device

    :param devip: str of ipv4 address of the target device

    :return: list of dictionaries where each element of the list represents an interface which
    has been configured as a
    VLAN access port

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> access_interfaces = get_device_access_interfaces('10', auth.creds, auth.url)

    >>> assert type(access_interfaces) is list

    >>> assert (len(access_interfaces[0])) is 2

    >>> assert 'ifIndex' in access_interfaces[0]

    >>> assert 'pvid' in access_interfaces[0]

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    get_access_interface_vlan_url = "/imcrs/vlan/access?devId=" + str(devid) + \
                                    "&start=1&size=500&total=false"
    f_url = url + get_access_interface_vlan_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_access_interfaces = (json.loads(response.text))
            if len(dev_access_interfaces) == 2:
                return dev_access_interfaces['accessIf']
            else:
                dev_access_interfaces['accessIf'] = ["No access inteface"]
                return dev_access_interfaces['accessIf']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_device_access_interfaces: An Error has occured"


# Section for Hybrid Interfaces - Applies to Comware Devices only

def get_device_hybrid_interfaces(auth, url, devid=None, devip=None):
    """
    Function takes devId as input to RESTFUL call to HP IMC platform

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid: str requires devid of the target device

    :param devip: str of ipv4 address of the target device

    :return: list of dictionaries where each element of the list represents an interface which
    has been configured as a
    VLAN access port

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> hybrid_interfaces = get_device_hybrid_interfaces('10', auth.creds, auth.url)

    >>> assert type(access_interfaces) is list

    >>> assert (len(access_interfaces[0])) is 2

    >>> assert 'ifIndex' in access_interfaces[0]

    >>> assert 'pvid' in access_interfaces[0]

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    get_hybrid_interface_vlan_url = "/imcrs/vlan/hybrid?devId=" + str(devid) + \
                                    "&start=1&size=500&total=false"
    f_url = url + get_hybrid_interface_vlan_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            dev_hybrid_interfaces = (json.loads(response.text))
            if len(dev_hybrid_interfaces) == 2:
                dev_hybrid = dev_hybrid_interfaces['hybridIf']
                if isinstance(dev_hybrid, dict):
                    dev_hybrid = [dev_hybrid]
                return dev_hybrid
            else:
                dev_hybrid_interfaces['hybridIf'] = ["No hybrid inteface"]
                return dev_hybrid_interfaces['hybridIf']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_device_hybrid_interfaces: An Error has occured"


def add_hybrid_interface(ifindex, pvid, taggedvlans, untaggedvlans, auth, url, devip=None,
                         devid=None):
    """
    Function takes ifindex, pvid, tagged vlans untagged vlans as input values to add a hybrid
    port to a HPE Comware based switch. These functions only apply to HPE Comware based devices.
    :param ifindex: str ifIndex value of target interface
    :param pvid: str 802.1q value (1-4094) of target VLAN
    :param taggedvlans:  str 802.1q value, seperated by commas, of target tagged VLANs
    :param untaggedvlans:  str 802.1q value, seperated by commas, of target untagged VLANs
    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class
    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass
    :param devid: str requires devid of the target device
    :param devip: str of ipv4 address of the target device
    :return int of http response code
    :rtype int
    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    add_hybrid_interface_url = "/imcrs/vlan/hybrid?devId=" + str(devid) +  \
                               "&start=1&size=500&total=false"
    f_url = url + add_hybrid_interface_url
    payload = '''{"ifIndex": "''' + ifindex + '''",
        "pvid": "''' + pvid + '''",
        "taggedVlans": "''' + taggedvlans + '''",
        "untagVlanFlag": "true",
        "untaggedVlans": "''' + untaggedvlans + '''"
    }'''
    response = requests.post(f_url, auth=auth, data=payload, headers=HEADERS)
    try:
        if response.status_code == 201:
            return 201
        if response.status_code == 409:
            return 409
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_device_hybrid_interfaces: An Error has occured"


def modify_hybrid_interface(ifindex, pvid, taggedvlans, untaggedvlans, auth, url, devip=None,
                            devid=None):
    """
        Function takes ifindex, pvid, tagged vlans untagged vlans as input values to modify a
        hybrid port to a HPE Comware based switch. These functions only apply to HPE Comware
        based devices.
        :param ifindex: str ifIndex value of target interface
        :param pvid: str 802.1q value (1-4094) of target VLAN
        :param taggedvlans:  str 802.1q value, seperated by commas, of target tagged VLANs
        :param untaggedvlans:  str 802.1q value, seperated by commas, of target untagged VLANs
        :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class
        :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass
        :param devid: str requires devid of the target device
        :param devip: str of ipv4 address of the target device
        :return int of http response code
        :rtype int
        """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    f_url = url + "/imcrs/vlan/hybrid?devId=" + str(devid) + "&start=1&size=500&total=false"
    payload = '''{"ifIndex": "''' + ifindex + '''",
        "pvid": "''' + pvid + '''",
        "taggedVlans": "''' + taggedvlans + '''",
        "untagVlanFlag": "true",
        "untaggedVlans": "''' + untaggedvlans + '''"
    }'''
    response = requests.put(f_url, auth=auth, data=payload, headers=HEADERS)
    try:
        if response.status_code == 204:
            return 204
        if response.status_code == 409:
            return 409
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_device_hybrid_interfaces: An Error has occured"


def delete_hybrid_interface(ifindex, auth, url, devip=None, devid=None):
    """
     Function takes devip ( ipv4 address ), ifIndex and pvid (vlanid) of specific device and
     802.1q VLAN tag and issues a RESTFUL call to remove the specified VLAN from the target device.

    :param ifindex: str value of ifIndex for a specific interface on the device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid: str requires devid of the target device

    :param devip: str of ipv4 address of the target device

    :return: int of 204 if successful or 409 if not succesful

    :rtype: int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> delete_hybrid_interface('9', auth.creds, auth.url, devip='10.101.0.221')
    409

    >>> add_hybrid = add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url,
                                           devip='10.101.0.221')

    >>> delete_hybrid = delete_hybrid_interface('9', auth.creds, auth.url, devip='10.101.0.221')

    >>> assert type(delete_hybrid) is int

    >>> assert delete_hybrid == 204
    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    f_url = url + "/imcrs/vlan/hybrid?devId=" + devid + "&ifIndex=" + ifindex
    response = requests.delete(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            return 204
        if response.status_code == 409:
            return 409
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_device_hybrid_interfaces: An Error has occured"


# Section for working with Access Interfaces

def set_access_interface_pvid(ifindex, pvid, auth, url, devip=None, devid=None):
    """
    Function takes devip ( ipv4 address ), ifIndex and pvid (vlanid) of specific device and
    802.1q VLAN tag and issues a RESTFUL call to remove the specified VLAN from the target device.

    :param ifindex: str value of ifIndex for a specific interface on the device

    :param pvid:  str value of dot1q VLAN desired to apply to the device

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid: str requires devid of the target device

    :param devip: str of ipv4 address of the target device

    :return: int of 204 if successful or 409 if not succesful

    :rtype: int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> set_access_int_vlan = set_access_interface_pvid('9', '1', auth.creds, auth.url,
                                                        devip='10.101.0.221')

    >>> set_access_int_vlan = set_access_interface_pvid('9', '10', auth.creds, auth.url,
                                                        devip='10.101.0.221')

    >>> assert type(set_access_int_vlan) is int

    >>> assert set_access_int_vlan == 204

    >>> set_access_int_vlan = set_access_interface_pvid('9', '1', auth.creds, auth.url,
                                                        devip='10.101.0.221')

    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    set_access_interface_pvid_url = "/imcrs/vlan/access?devId=" + devid + "&destVlanId=" + pvid \
                                    + "&ifIndex=" + str(ifindex)
    f_url = url + set_access_interface_pvid_url
    response = requests.put(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            return 204
        if response.status_code == 409:
            return 409
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " set_access_interface_pvid: An Error has occured"


def get_access_interface_vlan(ifindex, accessinterfacelist):
    """
    Function which takes input of str of ifIndex value for target interface and
    accessinterfacelist ( output of get_device_access_interfaces) to send against IMC REST
    interface. Function returns str representing the PVD of the target interface

    :param ifindex: str object representing the numeric value of the iFindex for the interface

    :param accessinterfacelist: list object, intended to be the output of the
    get_device_access_interfaces function

    :return: str representing the numeric value of the PVID for the target interface.

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> access_interface_list = get_device_access_interfaces(auth.creds, auth.url,
                                                             devip='10.101.0.221')

    >>> get_access_interface_vlan('4', access_interface_list, auth.creds, auth.url)
    '1'
    """
    for i in accessinterfacelist:
        if i['ifIndex'] == ifindex:
            return i['pvid']
        else:
            return "Not an Access Port"


def create_dev_vlan(vlanid, vlan_name, auth, url, devid=None, devip=None):
    """
    function takes devid and vlanid vlan_name of specific device and 802.1q VLAN tag
    and issues a RESTFUL call to add the specified VLAN from the target device. VLAN Name
    MUST be valid on target device.

    :param vlanid:int or str value of target 802.1q VLAN

    :param vlan_name: str value of the target 802.1q VLAN name. MUST be valid name on target device.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid: str requires devid of the target device

    :param devip: str of ipv4 address of the target device

    :return: str HTTP Response code. Should be 201 if successfully created

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> create_dev_vlan = create_dev_vlan('350', '200', 'test vlan', auth.creds, auth.url)


    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    create_dev_vlan_url = "/imcrs/vlan?devId=" + str(devid)
    f_url = url + create_dev_vlan_url
    payload = '''{"vlanId":"%s", "vlanName":"%s"}''' % (str(vlanid), vlan_name)
    response = requests.post(f_url, data=payload, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 201:
            print('Vlan Created')
            return 201
        elif response.status_code == 409:
            print('''Unable to create VLAN.\nVLAN Already Exists\nDevice does not support  VLAN
            function''')
            return 409
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " create_dev_vlan: An Error has occured"


def delete_dev_vlans(vlanid, auth, url, devid=None, devip=None):
    """
    function takes devid and vlanid of specific device and 802.1q VLAN tag and issues a RESTFUL
    call to remove the specified VLAN from the target device.
    :param vlanid:int or str value of target 802.1q VLAN

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: HTTP response object from requests library. Status code should be 204 if Successful

    :param devid: str requires devid of the target device

    :param devip: str of ipv4 address of the target device

    :rtype: requests.models.Response

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> create_dev_vlan = create_dev_vlan('350', '200', 'test vlan', auth.creds, auth.url)
    """
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    remove_dev_vlan_url = "/imcrs/vlan/delvlan?devId=" + str(devid) + "&vlanId=" + str(vlanid)
    f_url = url + remove_dev_vlan_url
    response = requests.delete(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            print('Vlan deleted')
            return response.status_code
        elif response.status_code == 409:
            print('Unable to delete VLAN.\nVLAN does not Exist\nDevice does not support  VLAN '
                  'function')
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " delete_dev_vlans: An Error has occured"
