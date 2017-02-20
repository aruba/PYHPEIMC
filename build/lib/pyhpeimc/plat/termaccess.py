#!/usr/bin/env python3
# author: @netmanchris



# This section imports required libraries
import json
import requests
import ipaddress


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}





def get_real_time_locate(ipAddress, auth, url):
    """
    function takes the ipAddress of a specific host and issues a RESTFUL call to get the device and interface that the
    target host is currently connected to. Note: Although intended to return a single location, Multiple locations may
    be returned for a single host due to a partially discovered network or misconfigured environment.

    :param ipAddress: str value valid IPv4 IP address

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents the location of the target host

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_real_time_locate('10.101.0.51', auth.creds, auth.url)
    [{'deviceId': '10',
  'deviceIp': '192.168.1.221',
  'ifDesc': 'GigabitEthernet1/0/2',
  'ifIndex': '2',
  'locateIp': '10.101.0.51'}]


    """
    real_time_locate_url = "/imcrs/res/access/realtimeLocate?type=2&value=" + str(ipAddress) + "&total=false"
    f_url = url + real_time_locate_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            response =  json.loads(r.text)
            if 'realtimeLocation' in response:
                real_time_locate = json.loads(r.text)['realtimeLocation']
                if type(real_time_locate) is dict:
                    real_time_locate = [real_time_locate]
                    return real_time_locate
                else:
                    return json.loads(r.text)['realtimeLocation']
            else:
                return json.loads(r.text)

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_real_time_locate: An Error has occured"


def get_ip_mac_arp_list(devId, auth,url):
    """
    function takes devid of specific device and issues a RESTFUL call to get the IP/MAC/ARP list from the target device.

    :param devId: int or str value of the target device.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries containing the IP/MAC/ARP list of the target device.

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_ip_mac_arp_list('10', auth.creds, auth.url)
    [{'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.10.10.5',
  'ifIndex': '39',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/39',
  'macAddress': 'd0:7e:28:80:40:0c'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.10.3.3',
  'ifIndex': '51',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/51',
  'macAddress': 'd0:7e:28:80:40:0c'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.10.3.5',
  'ifIndex': '51',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/51',
  'macAddress': 'd0:7e:28:80:40:0f'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.101.0.1',
  'ifIndex': '30',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/30',
  'macAddress': '00:1b:d4:47:1e:68'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.101.0.100',
  'ifIndex': '30',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/30',
  'macAddress': '00:50:56:66:7d:73'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.101.0.102',
  'ifIndex': '30',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/30',
  'macAddress': '14:99:e2:28:ec:24'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.101.0.105',
  'ifIndex': '30',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/30',
  'macAddress': '78:48:59:49:18:c0'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.101.0.107',
  'ifIndex': '30',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/30',
  'macAddress': '78:48:59:49:16:40'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.101.0.108',
  'ifIndex': '30',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/30',
  'macAddress': '2c:41:38:7f:a8:eb'},
 {'device': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10',
  'deviceId': '10',
  'deviceIp': '10.101.0.110',
  'ifIndex': '30',
  'iface': 'http://kontrolissues.thruhere.net:8086/imcrs/plat/res/device/10/interface/30',
  'macAddress': 'c0:cb:38:63:42:cd'}]

    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    ip_mac_arp_list_url = "/imcrs/res/access/ipMacArp/" + str(devId)
    f_url = url + ip_mac_arp_list_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            macarplist = (json.loads(r.text))
            if len(macarplist) > 1:
                return macarplist['ipMacArp']
            else:
                return ['this function is unsupported']

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_mac_arp_list: An Error has occured"


#this section deals with the IP Address Manager functions with terminal access of HPE IMC Base platform

def get_ip_scope(auth, url, scopeId=None,):
    """
    function requires no inputs and returns all IP address scopes currently configured on the HPE IMC server. If the
    optional scopeId parameter is included, this will automatically return only the desired scope id.

    :param scopeId: integer of the desired scope id ( optional )

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionary objects where each element of the list represents one IP scope

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_ip_scope(auth.creds, auth.url)
    [{'description': 'Allocated IP addresses that do not belong to any allocated IP segment.',
  'id': '-299',
  'ip': 'The system default IP segment',
  'name': 'Admin',
  'parentId': '-300',
  'percent': '0.0',
  'percentStr': '0.0%'},
 {'description': 'Management IP Segment',
  'endIp': '10.10.254.254',
  'id': '44',
  'ip': '10.10.0.1-10.10.254.254',
  'name': 'cyoung',
  'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2'],
  'parentId': '-300',
  'percent': '9.191458071632097E-5',
  'percentStr': '0.00%',
  'startIp': '10.10.0.1'},
 {'assignedIpScope': [{'description': 'Mobile First Management Subnet',
    'endIp': '10.11.10.254',
    'id': '168',
    'ip': '10.11.10.1-10.11.10.254',
    'name': 'cyoung',
    'parentId': '45',
    'percent': '0.003937007874015748',
    'percentStr': '0.39%',
    'rightIpId': '45',
    'startIp': '10.11.10.1'},
   {'description': 'Mobile First User Subnet',
    'endIp': '10.11.1.254',
    'id': '169',
    'ip': '10.11.1.1-10.11.1.254',
    'name': 'cyoung',
    'parentId': '45',
    'percent': '0.0',
    'percentStr': '0.0%',
    'rightIpId': '45',
    'startIp': '10.11.1.1'},
   {'description': 'Mobile First Server Subnet',
    'endIp': '10.11.20.254',
    'id': '170',
    'ip': '10.11.20.1-10.11.20.254',
    'name': 'cyoung',
    'parentId': '45',
    'percent': '0.0',
    'percentStr': '0.0%',
    'rightIpId': '45',
    'startIp': '10.11.20.1'}],
  'description': 'Mobile First Branch',
  'endIp': '10.11.254.254',
  'id': '45',
  'ip': '10.11.0.1-10.11.254.254',
  'name': 'cyoung',
  'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2'],
  'parentId': '-300',
  'percent': '1.5319096786053493E-5',
  'percentStr': '0.00%',
  'startIp': '10.11.0.1'},
 {'description': 'Cisco Branch',
  'endIp': '10.12.254.254',
  'id': '46',
  'ip': '10.12.0.1-10.12.254.254',
  'name': 'cyoung',
  'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1'],
  'parentId': '-300',
  'percent': '3.0638193572106986E-5',
  'percentStr': '0.00%',
  'startIp': '10.12.0.1'},
 {'description': 'DataCenter',
  'endIp': '10.20.254.254',
  'id': '47',
  'ip': '10.20.0.1-10.20.254.254',
  'name': 'cyoung',
  'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1'],
  'parentId': '-300',
  'percent': '1.5319096786053493E-5',
  'percentStr': '0.00%',
  'startIp': '10.20.0.1'},
 {'assignedIpScope': [{'description': 'default production segment',
    'endIp': '10.101.0.254',
    'id': '67',
    'ip': '10.101.0.1-10.101.0.254',
    'name': 'cyoung',
    'parentId': '48',
    'percent': '0.41732283464566927',
    'percentStr': '41.73%',
    'rightIpId': '48',
    'startIp': '10.101.0.1'},
   {'description': 'Phone IP Segment',
    'endIp': '10.101.16.254',
    'id': '69',
    'ip': '10.101.16.1-10.101.16.254',
    'name': 'cyoung',
    'parentId': '48',
    'percent': '0.003937007874015748',
    'percentStr': '0.39%',
    'rightIpId': '48',
    'startIp': '10.101.16.1'},
   {'description': 'test child func',
    'endIp': '10.101.17.254',
    'id': '70',
    'ip': '10.101.17.1-10.101.17.254',
    'name': 'cyoung',
    'parentId': '48',
    'percent': '0.0',
    'percentStr': '0.0%',
    'rightIpId': '48',
    'startIp': '10.101.17.1'},
   {'description': 'test range 2',
    'endIp': '10.101.18.24',
    'id': '71',
    'ip': '10.101.18.1-10.101.18.24',
    'name': 'cyoung',
    'parentId': '48',
    'percent': '0.0',
    'percentStr': '0.0%',
    'rightIpId': '48',
    'startIp': '10.101.18.1'}],
  'description': 'Main Branch',
  'endIp': '10.101.254.254',
  'id': '48',
  'ip': '10.101.0.1-10.101.254.254',
  'name': 'cyoung',
  'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3'],
  'parentId': '-300',
  'percent': '0.001669781549679831',
  'percentStr': '0.16%',
  'startIp': '10.101.0.1'},
 {'description': 'Juniper Branch',
  'endIp': '10.13.254.254',
  'id': '165',
  'ip': '10.13.0.1-10.13.254.254',
  'name': 'cyoung',
  'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2'],
  'parentId': '-300',
  'percent': '0.0',
  'percentStr': '0.0%',
  'startIp': '10.13.0.1'},
 {'description': 'Comware5 Branch',
  'endIp': '10.14.254.254',
  'id': '166',
  'ip': '10.14.0.1-10.14.254.254',
  'name': 'cyoung',
  'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1'],
  'parentId': '-300',
  'percent': '0.0',
  'percentStr': '0.0%',
  'startIp': '10.14.0.1'},
 {'assignedIpScope': [{'description': 'P2P Link between Cloud First Datacenter and Mobile First Branch',
    'endIp': '172.16.0.2',
    'id': '171',
    'ip': '172.16.0.1-172.16.0.2',
    'name': 'cyoung',
    'parentId': '167',
    'percent': '0.0',
    'percentStr': '0.0%',
    'rightIpId': '167',
    'startIp': '172.16.0.1'},
   {'description': 'P2P Link between Cloud First Data Center and Juniper Branch',
    'endIp': '172.16.0.6',
    'id': '172',
    'ip': '172.16.0.5-172.16.0.6',
    'name': 'cyoung',
    'parentId': '167',
    'percent': '0.0',
    'percentStr': '0.0%',
    'rightIpId': '167',
    'startIp': '172.16.0.5'},
   {'description': 'P2P Link between Cloud First Datacenter and HPE FlexFabric Branch',
    'endIp': '172.16.0.10',
    'id': '173',
    'ip': '172.16.0.9-172.16.0.10',
    'name': 'cyoung',
    'parentId': '167',
    'percent': '0.0',
    'percentStr': '0.0%',
    'rightIpId': '167',
    'startIp': '172.16.0.9'},
   {'description': 'P2P Link between Cloud First Datacenter and Cisco Branch',
    'endIp': '172.16.0.14',
    'id': '174',
    'ip': '172.16.0.13-172.16.0.14',
    'name': 'cyoung',
    'parentId': '167',
    'percent': '0.0',
    'percentStr': '0.0%',
    'rightIpId': '167',
    'startIp': '172.16.0.13'}],
  'description': 'WAN P2P Links',
  'endIp': '172.16.30.254',
  'id': '167',
  'ip': '172.16.0.0-172.16.30.254',
  'name': 'cyoung',
  'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3',
   'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1'],
  'parentId': '-300',
  'percent': '0.0',
  'percentStr': '0.0%',
  'startIp': '172.16.0.0'}]

    """
    if scopeId is None:
        get_ip_scope_url = "/imcrs/res/access/assignedIpScope"
    else:
        get_ip_scope_url = "/imcrs/res/access/assignedIpScope/ip?ipScopeId="+str(scopeId)

    f_url = url + get_ip_scope_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            ipscopelist = (json.loads(r.text))
            return ipscopelist['assignedIpScope']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_scope: An Error has occured"

def get_ip_scope_detail(scopeId, auth, url ):
    """
    function requires no inputs and returns all IP address scopes currently configured on the HPE IMC server. If the
    optional scopeId parameter is included, this will automatically return only the desired scope id.
    :param scopeId: integer of the desired scope id ( optional )

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: dictionary, may containing multiple entries if sub-scopes have been created

    :rtype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_ip_scope_detail('45', auth.creds, auth.url)
    {'assignedIpScope': [{'description': 'Mobile First Management Subnet',
   'endIp': '10.11.10.254',
   'id': '168',
   'ip': '10.11.10.1-10.11.10.254',
   'name': 'cyoung',
   'parentId': '45',
   'percent': '0.003937007874015748',
   'percentStr': '0.39%',
   'rightIpId': '45',
   'startIp': '10.11.10.1'},
  {'description': 'Mobile First User Subnet',
   'endIp': '10.11.1.254',
   'id': '169',
   'ip': '10.11.1.1-10.11.1.254',
   'name': 'cyoung',
   'parentId': '45',
   'percent': '0.0',
   'percentStr': '0.0%',
   'rightIpId': '45',
   'startIp': '10.11.1.1'},
  {'description': 'Mobile First Server Subnet',
   'endIp': '10.11.20.254',
   'id': '170',
   'ip': '10.11.20.1-10.11.20.254',
   'name': 'cyoung',
   'parentId': '45',
   'percent': '0.0',
   'percentStr': '0.0%',
   'rightIpId': '45',
   'startIp': '10.11.20.1'}],
 'description': 'Mobile First Branch',
 'endIp': '10.11.254.254',
 'id': '45',
 'ip': '10.11.0.1-10.11.254.254',
 'name': 'cyoung',
 'operatorGroup': ['http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/1',
  'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/2',
  'http://kontrolissues.thruhere.net:8086/imcrs/plat/operatorGroup/3'],
 'parentId': '-300',
 'percent': '1.5319096786053493E-5',
 'percentStr': '0.00%',
 'startIp': '10.11.0.1'}

    """
    get_ip_scope_url = "/imcrs/res/access/assignedIpScope/"+str(scopeId)

    f_url = url + get_ip_scope_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            ipscopelist = (json.loads(r.text))
            return ipscopelist
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_scope: An Error has occured"


def get_ip_scope_hosts( scopeId, auth, url):
    """
    Function requires input of scope ID and returns list of allocated IP address for the specified scope

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param scopeId: Interger of teh desired scope id

    :return: list of dictionary objects where each element of the list represents a single host assigned to the IP scope

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_ip_scope_hosts('45', auth.creds, auth.url)
    [{'description': 'HP MSR930',
  'id': '31',
  'ip': '10.11.10.1',
  'name': 'R1Br4Core',
  'parentId': '168'}]

    """
    get_ip_scope_url = "/imcrs/res/access/assignedIpScope/ip?size=10000&ipScopeId="+str(scopeId)
    f_url = url + get_ip_scope_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            ipscopelist = (json.loads(r.text))
            ipscopelist = ipscopelist['assignedIpInfo']
            if type(ipscopelist) is dict:
                ipscope = []
                ipscope.append(ipscopelist)
                return ipscope
            return ipscopelist
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_scope: An Error has occured"


def add_ip_scope(startIp, endIp, name, description, auth, url):
    """
    Function takes input of four strings Start Ip, endIp, name, and description to add new Ip Scope to terminal access
    in the HPE IMC base platform

    :param startIp: str Start of IP address scope ex. '10.101.0.1'

    :param endIp: str End of IP address scope ex. '10.101.0.254'

    :param name: str Name of the owner of this IP scope  ex. 'admin'

    :param description: str description of the Ip scope

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: 200 if successfull

    :rtype:

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)
    IP Scope Successfully Created
    200


    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()

    add_ip_scope_url = "/imcrs/res/access/assignedIpScope"
    f_url = url + add_ip_scope_url
    payload = ('''{  "startIp": "%s", "endIp": "%s","name": "%s","description": "%s" }'''
               %(str(startIp), str(endIp), str(name), str(description)))
    r = requests.post(f_url, auth=auth, headers=HEADERS, data=payload) # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print ("IP Scope Already Exists")
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"

def add_child_ip_scope(startIp, endIp, name, description, scopeid, auth, url):
    """
    Function takes input of four strings Start Ip, endIp, name, and description to add new Ip Scope to terminal access
    in the HPE IMC base platform

    :param startIp: str Start of IP address scope ex. '10.101.0.1'

    :param endIp: str End of IP address scope ex. '10.101.0.254'

    :param name: str Name of the owner of this IP scope  ex. 'admin'

    :param description: str description of the Ip scope

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: 200

    :rtype:

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> add_child_ip_scope('10.50.0.1', '10.50.0.126', 'cyoung', 'test sub scope', '175', auth.creds, auth.url)
    IP Scope Successfully Created
    200


    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()

    add_ip_scope_url = "/imcrs/res/access/assignedIpScope/" + str(scopeid)
    f_url = url + add_ip_scope_url
    payload = ('''{  "startIp": "%s", "endIp": "%s","name": "%s","description": "%s", "parentId" : "%s"}'''
               %(str(startIp), str(endIp), str(name), str(description), str(scopeid)))
    r = requests.post(f_url, auth=auth, headers=HEADERS, data=payload) # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print ("Conflict with Current Scope")
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"

def add_scope_ip(ipaddress, name, description, scopeid, auth, url):
    """
    Function to add new host IP address allocation to existing scope ID

    :param ipaddress:

    :param name: name of the owner of this host

    :param description: Description of the host

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return:

    :rtype:

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> add_scope_ip('10.50.0.5', 'cyoung', 'New Test Host','175', auth.creds, auth.url)

    """
    new_ip = { "ip": ipaddress,
      "name": name,
      "description": description}
    add_scope_ip_url = '/imcrs/res/access/assignedIpScope/ip?ipScopeId='+str(scopeid)
    f_url = url + add_scope_ip_url
    payload = json.dumps(new_ip)
    r = requests.post(f_url, auth=auth, headers=HEADERS,
                      data=payload)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print("IP Scope Already Exists")
            return r.status_code
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"

def remove_scope_ip(hostid, auth, url):
    """
    Function to add new IP address allocation to existing scope ID

    :param hostid: Host id of the host to be deleted

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: String of HTTP response code. Should be 204 is successfull

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> remove_scope_ip('177', auth.creds, auth.url)
    204

    """
    add_scope_ip_url = '/imcrs/res/access/assignedIpScope/ip/'+str(hostid)
    f_url = url + add_scope_ip_url

    r = requests.delete(f_url, auth=auth, headers=HEADERS,
                      )
    try:
        if r.status_code == 204:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print("IP Scope Already Exists")
            return r.status_code
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"



def get_scope_id(network_address, auth, url):
    """

    :param network_address: network address of the target scope in format x.x.x.x/yy  where x.x.x.x representents the
    network address and yy represents the length of the subnet mask.  Example:  10.50.0.0 255.255.255.0 would be written
    as 10.50.0.0/24

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str object which contains the numerical ID of the target scope

    :rtype: str


    >>>get_scope_id('10.50.0.0/24', auth.creds, auth.url)
    '175'

    """
    netaddr = ipaddress.ip_network(network_address)
    scopes = get_ip_scope(auth, url)
    for i in scopes:
        if int(i['id']) > 0:
            if ipaddress.ip_address(i['startIp']) in netaddr and ipaddress.ip_address(i['endIp']) in netaddr:
                return i['id']
            if "assignedIpScope" in i:
                for child in i['assignedIpScope']:
                    if ipaddress.ip_address(child['startIp']) in netaddr and ipaddress.ip_address(child['endIp']) in netaddr:

                        return child['id']









    #Add host to IP scope
    #http://10.101.0.203:8080/imcrs/res/access/assignedIpScope/ip?ipScopeId=1
    '''{
      "ip": "10.101.0.1",
      "name": "Cisco2811.lab.local",
      "description": "Cisco 2811",
      "parentId": "18"
    }'''