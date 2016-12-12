#!/usr/bin/env python3
# author: @netmanchris



# This section imports required libraries
import requests
import json
from pyhpeimc.plat.device import get_dev_details


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

#command creates dummy IMCAuth object. Should be overwritten in script calling these functions



"""
This section contains functions which operate at the device level
"""
def get_dev_vlans(auth, url, devid = None, devip= None):
    """Function takes input of devID to issue RESTUL call to HP IMC

    :param devid: str requires devId as the only input parameter

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents one vlan on the target device

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> vlans = get_dev_vlans('350', auth.creds, auth.url)

    >>> assert type(vlans) is list

    >>> assert 'vlanId' in vlans[0]

    """
    if devip is not None:
        devid=get_dev_details(devip, auth, url)['id']
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


def get_trunk_interfaces( auth, url, devId=None, devip=None ):
    """Function takes devId as input to RESTFULL call to HP IMC platform

    :param devid: str requires devId as the only input parameter

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents an interface which has been configured as a
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
        devId=get_dev_details(devip, auth, url)['id']
    # checks to see if the imc credentials are already available
    get_trunk_interfaces_url = "/imcrs/vlan/trunk?devId=" + str(devId) + "&start=1&size=5000&total=false"
    f_url = url + get_trunk_interfaces_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)
    # r.status_code
    print (f_url)
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


def get_device_access_interfaces(auth, url, devId=None, devip = None):
    """Function takes devId as input to RESTFUL call to HP IMC platform
    :param devid: str requires devId as the only input parameter

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents an interface which has been configured as a
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
        devId=get_dev_details(devip, auth, url)['id']
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
    """

    :param ifIndex: str object representing the numeric value of the iFindex for the interface

    :param accessinterfacelist: list object, intended to be the output of the get_device_access_interfaces function

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str representing the numeric value of the PVID for the target interface.

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> access_interface_list = get_device_access_interfaces('10', auth.creds, auth.url)

    >>> get_access_interface_vlan('4', access_interface_list, auth.creds, auth.url)
    '1'
    """
    for i in accessinterfacelist:
        if i['ifIndex'] == ifIndex:
            return i['pvid']
        else:
            return "Not an Access Port"


#TODO add abstraction to use IP address of device and not
def create_dev_vlan( vlanid, vlan_name, auth, url, devid= None, devip = None ):
    """
    function takes devid and vlanid vlan_name of specific device and 802.1q VLAN tag and issues a RESTFUL call to add the
    specified VLAN from the target device. VLAN Name MUST be valid on target device.

    :param devid: int or str value of the target device

    :param vlanid:int or str value of target 802.1q VLAN

    :param vlan_name: str value of the target 802.1q VLAN name. MUST be valid name on target device.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str HTTP Response code. Should be 201 if successfully created

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> create_dev_vlan = create_dev_vlan('350', '200', 'test vlan', auth.creds, auth.url)


    """
    if devip is not None:
        devid=get_dev_details(devip, auth, url)['id']
    create_dev_vlan_url = "/imcrs/vlan?devId=" + str(devid)
    f_url = url + create_dev_vlan_url
    print (f_url)
    payload = '''{ "vlanId": "''' + str(vlanid) + '''", "vlanName" : "''' + str(vlan_name) + '''"}'''
    print (payload)
    r = requests.post(f_url, data=payload, auth=auth,
                      headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:

        if r.status_code == 201:
            print ('Vlan Created')
            return 201
        elif r.status_code == 409:
            print ('''Unable to create VLAN.\nVLAN Already Exists\nDevice does not support VLAN function''')
            return 409
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " create_dev_vlan: An Error has occured"


def delete_dev_vlans(vlanid, auth, url, devid=None, devip=None):
    """
    function takes devid and vlanid of specific device and 802.1q VLAN tag and issues a RESTFUL call to remove the
    specified VLAN from the target device.
    :param vlanid:int or str value of target 802.1q VLAN

    :param vlan_name: str value of the target 802.1q VLAN name. MUST be valid name on target device.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: HTTP response object from requests library. Status code should be 204 if Successful

    :rtype: requests.models.Response

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> create_dev_vlan = create_dev_vlan('350', '200', 'test vlan', auth.creds, auth.url)
    """
    if devip is not None:
        devid=get_dev_details(devip, auth, url)['id']
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