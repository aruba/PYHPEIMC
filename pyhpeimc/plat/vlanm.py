#!/usr/bin/env python3
# author: @netmanchris



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

    :param devid: str requires devId as the only input parameter

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents one vlan on the target device

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_dev_vlans('350', auth.creds, auth.url)
    [{'vlanId': '1', 'vlanName': 'default', 'vlanStatus': '1'},
 {'vlanId': '5', 'vlanName': 'DoesntBelong', 'vlanStatus': '1'}]

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

    :param devid: str requires devId as the only input parameter

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents an interface which has been configured as a
    VLAN trunk port

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_trunk_interfaces('10', auth.creds, auth.url)
    [{'allowedVlans': '1-4094', 'ifIndex': '1', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '2', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '3', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '5', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '6', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '7', 'pvid': '1'},
 {'allowedVlans': '1-2,110,500-503', 'ifIndex': '8', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '11', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '12', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '14', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '18', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '19', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '23', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '24', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '32', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '56', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '58', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '59', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '60', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '61', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '62', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '63', 'pvid': '1'},
 {'allowedVlans': '1-4094', 'ifIndex': '64', 'pvid': '1'},
 {'allowedVlans': '1,502-503', 'ifIndex': '78', 'pvid': '1'}]
    #example of a switch with no trunk interfaces configured
    >>> get_trunk_interfaces('350', auth.creds, auth.url)
    ['No trunk inteface']
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
    :param devid: str requires devId as the only input parameter

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents an interface which has been configured as a
    VLAN access port

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_device_access_interfaces('10', auth.creds, auth.url)
    [{'ifIndex': '4', 'pvid': '1'},
 {'ifIndex': '9', 'pvid': '1'},
 {'ifIndex': '10', 'pvid': '1'},
 {'ifIndex': '13', 'pvid': '1'},
 {'ifIndex': '20', 'pvid': '3010'},
 {'ifIndex': '21', 'pvid': '1'},
 {'ifIndex': '25', 'pvid': '1'},
 {'ifIndex': '26', 'pvid': '1'},
 {'ifIndex': '27', 'pvid': '1'},
 {'ifIndex': '28', 'pvid': '1'},
 {'ifIndex': '31', 'pvid': '1'},
 {'ifIndex': '50', 'pvid': '1'},
 {'ifIndex': '65', 'pvid': '1'},
 {'ifIndex': '66', 'pvid': '1'},
 {'ifIndex': '67', 'pvid': '1'},
 {'ifIndex': '68', 'pvid': '1'},
 {'ifIndex': '73', 'pvid': '1'},
 {'ifIndex': '74', 'pvid': '1'},
 {'ifIndex': '77', 'pvid': '1'},
 {'ifIndex': '79', 'pvid': '1'},
 {'ifIndex': '80', 'pvid': '1'},
 {'ifIndex': '81', 'pvid': '1'},
 {'ifIndex': '82', 'pvid': '1'},
 {'ifIndex': '83', 'pvid': '1'},
 {'ifIndex': '84', 'pvid': '1'},
 {'ifIndex': '86', 'pvid': '1'},
 {'ifIndex': '87', 'pvid': '1'},
 {'ifIndex': '88', 'pvid': '1'},
 {'ifIndex': '89', 'pvid': '1'},
 {'ifIndex': '90', 'pvid': '1'}]

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
    """
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

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str HTTP Response code. Should be 201 if successfully created

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vlanm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> create_dev_vlan = create_dev_vlan('350', '200', 'test vlan', auth.creds, auth.url)
    <Response [201]>


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