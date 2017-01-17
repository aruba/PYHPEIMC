#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the terminal access
capabilities, including IP Address management of the HPE IMC NMS
platform using the RESTful API

"""

# This section imports required libraries
import ipaddress
import json

import requests

from pyhpeimc.auth import HEADERS
from pyhpeimc.plat.device import get_dev_details

#pylint: disable=R0913

def get_real_time_locate(host_ipaddress, auth, url):
    """
    function takes the ipAddress of a specific host and issues a RESTFUL call to get the device and
    interface that the target host is currently connected to. Note: Although intended to return a
    single location, Multiple locations may be returned for a single host due to a partially
    discovered network or misconfigured environment.

    :param host_ipaddress: str value valid IPv4 IP address

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents the location of the
    target host

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> found_device = get_real_time_locate('10.101.0.51', auth.creds, auth.url)

    >>> assert type(found_device) is list

    >>> assert 'deviceId' in found_device[0]

    >>> assert 'deviceId' in found_device[0]

    >>> assert 'deviceId' in found_device[0]

    >>> assert 'deviceId' in found_device[0]

    >>> no_device = get_real_time_locate('192.168.254.254', auth.creds, auth.url)

    >>> assert type(no_device) is dict

    >>> assert len(no_device) == 0

    """
    f_url = url + "/imcrs/res/access/realtimeLocate?type=2&value=" + str(host_ipaddress)  + \
            "&total=false"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            response = json.loads(response.text)
            if 'realtimeLocation' in response:
                real_time_locate = response['realtimeLocation']
                if isinstance(real_time_locate, dict):
                    real_time_locate = [real_time_locate]
                    return real_time_locate
                else:
                    return json.loads(response)['realtimeLocation']
            else:
                print("Host not found")
                return 403
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_real_time_locate: An Error has occured"


def get_ip_mac_arp_list(auth, url, devid=None, devip=None):
    """
    function takes devid of specific device and issues a RESTFUL call to get the IP/MAC/ARP list
    from the target device.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param devid: int or str value of the target device.

    :param devip: str of ipv4 address of the target device

    :return: list of dictionaries containing the IP/MAC/ARP list of the target device.

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> ip_mac_list = get_ip_mac_arp_list( auth.creds, auth.url, devid='10')

    >>> ip_mac_list = get_ip_mac_arp_list( auth.creds, auth.url, devip='10.101.0.221')

    >>> assert type(ip_mac_list) is list

    >>> assert 'deviceId' in ip_mac_list[0]

    """
    if devip is not None:
        dev_details = get_dev_details(devip, auth, url)
        if isinstance(dev_details, str):
            print("Device not found")
            return 403
        else:
            devid = get_dev_details(devip, auth, url)['id']
    f_url = url + "/imcrs/res/access/ipMacArp/" + str(devid)
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            ipmacarplist = (json.loads(response.text))
            if 'ipMacArp' in ipmacarplist:
                return ipmacarplist['ipMacArp']
            else:
                return ['this function is unsupported']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ip_mac_arp_list: An Error has occured"


# this section deals with the IP Address Manager functions with terminal access of HPE IMC Base
# platform


# Following functions deal with IP scopes
def get_ip_scope(auth, url, scopeid=None, ):
    """
    function requires no inputs and returns all IP address scopes currently configured on the HPE
    IMC server. If the optional scopeid parameter is included, this will automatically return
    only the desired scope id.

    :param scopeid: integer of the desired scope id ( optional )

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionary objects where each element of the list represents one IP scope

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> ip_scope_list = get_ip_scope(auth.creds, auth.url)

    >>> assert type(ip_scope_list) is list

    >>> assert 'ip' in ip_scope_list[0]

    """
    if scopeid is None:
        get_ip_scope_url = "/imcrs/res/access/assignedIpScope"
    else:
        get_ip_scope_url = "/imcrs/res/access/assignedIpScope/ip?ipScopeId=" + str(scopeid)

    f_url = url + get_ip_scope_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            ipscopelist = (json.loads(response.text))
            return ipscopelist['assignedIpScope']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ip_scope: An Error has occured"


def get_ip_scope_detail(auth, url, scopeid=None, network_address=None):
    """
    function requires no inputs and returns all IP address scopes currently configured on the HPE
    IMC server. If the optional scopeId parameter is included, this will automatically return
    only the desired scope id.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param scopeid: integer of the desired scope id ( optional )

    :param network_address: ipv4 network address + subnet bits of target scope

    :return: dictionary, may containing multiple entries if sub-scopes have been created

    :rtype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> ip_scope_detail = get_ip_scope_detail( auth.creds, auth.url, scopeId = '45')

    >>> assert type(ip_scope_detail) is dict

    >>> assert 'startIp' in ip_scope_detail

    """
    if network_address is not None:
        scopeid = get_scope_id(network_address, auth, url)
    f_url = url + "/imcrs/res/access/assignedIpScope/" + str(scopeid)
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            ipscopelist = (json.loads(response.text))
            return ipscopelist
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ip_scope: An Error has occured"


def add_ip_scope(name, description, auth, url, startip=None, endip=None, network_address=None):
    """
    Function takes input of four strings Start Ip, endIp, name, and description to add new Ip Scope
    to terminal access in the HPE IMC base platform

    :param name: str Name of the owner of this IP scope  ex. 'admin'

    :param description: str description of the Ip scope

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param startip: str Start of IP address scope ex. '10.101.0.1'

    :param endip: str End of IP address scope ex. '10.101.0.254'

    :param network_address: ipv4 network address + subnet bits of target scope

    :return: 200 if successfull

    :rtype:

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> delete_ip_scope('10.50.0.0/24', auth.creds, auth.url)
    <Response [204]>

    >>> new_scope = add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)

    >>> assert type(new_scope) is int

    >>> assert new_scope == 200

    >>> existing_scope = add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)

    >>> assert type(existing_scope) is int

    >>> assert existing_scope == 409


    """
    if network_address is not None:
        nw_address = ipaddress.IPv4Network(network_address)
        startip = nw_address[1]
        endip = nw_address[-2]
    f_url = url + "/imcrs/res/access/assignedIpScope"
    payload = ('''{  "startIp": "%s", "endIp": "%s","name": "%s","description": "%s" }'''
               % (str(startip), str(endip), str(name), str(description)))
    response = requests.post(f_url, auth=auth, headers=HEADERS, data=payload)
    try:
        if response.status_code == 200:
            # print("IP Scope Successfully Created")
            return response.status_code
        elif response.status_code == 409:
            # print ("IP Scope Already Exists")
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " add_ip_scope: An Error has occured"


def add_child_ip_scope(name, description, auth, url, startip=None, endip=None, parent_scopeid=None,
                       network_address=None, parent_network_address=None):
    """
    Function takes input of four strings Start Ip, endIp, name, and description to add new Ip Scope
    to terminal access in the HPE IMC base platform

    :param name: str Name of the owner of this IP scope  ex. 'admin'

    :param description: str description of the Ip scope

    :param parent_scopeid: str or int of the scopeid of the target scope

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param startip: str Start of IP address scope ex. '10.101.0.1'

    :param endip: str End of IP address scope ex. '10.101.0.254'

    :param network_address: ipv4 network address + subnet bits of target scope

    :param parent_network_address: ipv4 network address + subnet bits of target parent scope

    :return: 200

    :rtype:

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> add_child_ip_scope('10.50.0.1', '10.50.0.126', 'cyoung', 'test sub scope', '175', auth.creds, auth.url)

    """
    if parent_network_address is not None:
        parent_scopeid = get_scope_id(parent_network_address, auth, url)
    if network_address is not None:
        nw_address = ipaddress.IPv4Network(network_address)
        startip = nw_address[1]
        endip = nw_address[-2]
    f_url = url + "/imcrs/res/access/assignedIpScope/" + str(parent_scopeid)
    payload = ('''{ "startIp": "%s", "endIp": "%s","name": "%s","description": "%s",
                    "parentId" : "%s"}'''
               % (str(startip), str(endip), str(name), str(description), str(parent_scopeid)))
    response = requests.post(f_url, auth=auth, headers=HEADERS, data=payload)
    try:
        if response.status_code == 200:
            # print("IP Scope Successfully Created")
            return response.status_code
        elif response.status_code == 409:
            # print ("Conflict with Current Scope")
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " add_ip_scope: An Error has occured"


def delete_ip_scope(network_address, auth, url):
    """
    Function to delete an entire IP segment from the IMC IP Address management under terminal access
    :param network_address
    :param auth
    :param url

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> new_scope = add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)

    >>> delete_scope = delete_ip_scope('10.50.0.0/24', auth.creds, auth.url)


    """
    scope_id = get_scope_id(network_address, auth, url)
    if scope_id == "Scope Doesn't Exist":
        return scope_id
    f_url = url + '''/imcrs/res/access/assignedIpScope/''' + str(scope_id)
    response = requests.delete(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            # print("IP Segment Successfully Deleted")
            return 204
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " delete_ip_scope: An Error has occured"


# Following functions deal with hosts assigned to IP scopes

def add_scope_ip(hostipaddress, name, description, auth, url, scopeid=None, network_address=None):
    """
    Function to add new host IP address allocation to existing scope ID

    :param hostipaddress: ipv4 address of the target host to be added to the target scope

    :param name: name of the owner of this host

    :param description: Description of the host

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param scopeid: integer of the desired scope id ( optional )

    :param network_address: ipv4 network address + subnet bits of target scope

    :return:

    :rtype:

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> new_host = add_scope_ip('10.50.0.5', 'cyoung', 'New Test Host','175', auth.creds, auth.url)

    """
    if network_address is not None:
        scopeid = get_scope_id(network_address, auth, url)
        if scopeid == "Scope Doesn't Exist":
            return scopeid
    new_ip = {"ip": hostipaddress,
              "name": name,
              "description": description}
    f_url = url + '/imcrs/res/access/assignedIpScope/ip?ipScopeId=' + str(scopeid)
    payload = json.dumps(new_ip)
    response = requests.post(f_url, auth=auth, headers=HEADERS, data=payload)
    try:
        if response.status_code == 200:
            # print("IP Host Successfully Created")
            return response.status_code
        elif response.status_code == 409:
            # print("IP Host Already Exists")
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " add_ip_scope: An Error has occured"


def remove_scope_ip(hostid, auth, url):
    """
    Function to add remove IP address allocation

    :param hostid: Host id of the host to be deleted

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: String of HTTP response code. Should be 204 is successfull

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> new_scope = add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)

    >>> add_host_to_segment('10.50.0.5', 'cyoung', 'New Test Host', '10.50.0.0/24', auth.creds, auth.url)

    >>> host_id = get_host_id('10.50.0.5', '10.50.0.0/24', auth.creds, auth.url)

    >>> rem_host = remove_scope_ip(host_id, auth.creds, auth.url)

    >>> assert type(rem_host) is int

    >>> assert rem_host == 204

    """
    f_url = url + '/imcrs/res/access/assignedIpScope/ip/' + str(hostid)
    response = requests.delete(f_url, auth=auth, headers=HEADERS, )
    try:
        if response.status_code == 204:
            # print("Host Successfully Deleted")
            return response.status_code
        elif response.status_code == 409:
            # print("IP Scope Already Exists")
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " add_ip_scope: An Error has occured"


def get_ip_scope_hosts(auth, url, scopeid=None, network_address=None):
    """
    Function requires input of scope ID and returns list of allocated IP address for the
    specified scope

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param scopeid: Integer of the desired scope id

    :param network_address: ipv4 network address + subnet bits of target scope

    :return: list of dictionary objects where each element of the list represents a single host
    assigned to the IP scope

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> scope_id = get_scope_id('10.50.0.0/24', auth.creds, auth.url)

    >>> ip_scope_hosts = get_ip_scope_hosts(scope_id, auth.creds, auth.url)

    >>> assert type(ip_scope_hosts) is list

    >>> assert 'name' in ip_scope_hosts[0]

    >>> assert 'description' in ip_scope_hosts[0]

    >>> assert 'ip' in ip_scope_hosts[0]

    >>> assert 'id' in ip_scope_hosts[0]

    """
    if network_address is not None:
        scopeid = get_scope_id(network_address, auth, url)
        if scopeid == "Scope Doesn't Exist":
            return scopeid
    f_url = url + "/imcrs/res/access/assignedIpScope/ip?size=10000&ipScopeId=" + str(scopeid)
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            ipscopelist = (json.loads(response.text))
            if ipscopelist == {}:
                return ipscopelist
            else:
                ipscopelist = ipscopelist['assignedIpInfo']
            if isinstance(ipscopelist, dict):
                ipscope = [ipscopelist]
                return ipscope
            return ipscopelist
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ip_scope: An Error has occured"


def add_host_to_segment(hostipaddress, name, description, network_address, auth, url):
    """
    Function to abstract existing add_scope_ip_function. Allows for use of network address rather
    than forcing human to learn the scope_id
    :param hostipaddress: str ipv4 address of target host to be added to target scope

    :param name: name of the owner of this host

    :param description: Description of the host

    :param network_address: ipv4 network address + subnet bits of target scope

    :param: network_address: network address of the target scope in format x.x.x.x/yy  where
    x.x.x.x  representents the network address and yy represents the length of the subnet mask.
    Example:  10.50.0.0 255.255.255.0 would be written as 10.50.0.0/24

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return:

    :rtype:

    """
    scope_id = get_scope_id(network_address, auth, url)
    add_scope_ip(hostipaddress, name, description, scope_id, auth, url)


def delete_host_from_segment(hostipaddress, networkaddress, auth, url):
    """
    :param hostipaddress: str ipv4 address of the target host to be deleted

    :param networkaddress: ipv4 network address + subnet bits of target scope

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: String of HTTP response code. Should be 204 is successfull

    :rtype: str

    """
    host_id = get_host_id(hostipaddress, networkaddress, auth, url)
    delete_host = remove_scope_ip(host_id, auth, url)
    return delete_host



# Following Section are Helper functions to help translate human readable IPv4 address to IMC
# internal keys for working with IPscopes and hosts


def get_scope_id(network_address, auth, url):
    """

    :param network_address: network address of the target scope in format x.x.x.x/yy  where
    x.x.x.x  representents the network address and yy represents the length of the subnet mask.
    Example:  10.50.0.0 255.255.255.0 would be written as 10.50.0.0/24

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str object which contains the numerical ID of the target scope

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> new_scope = add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)

    >>> scope_id = get_scope_id('10.50.0.0/24', auth.creds, auth.url)


    >>> assert type(scope_id) is str

    """
    netaddr = ipaddress.ip_network(network_address)
    scopes = get_ip_scope(auth, url)
    for parent_scope in scopes:
        if int(parent_scope['id']) > 0:
            if "assignedIpScope" in parent_scope:
                child_scope = parent_scope['assignedIpScope']
                if isinstance(child_scope, dict):
                    child_scope = [child_scope]
                for scope in child_scope:
                    if ipaddress.ip_address(scope['startIp']) == netaddr[1] \
                            and ipaddress.ip_address(scope['endIp']) == netaddr[-2]:
                        return scope['id']
            if ipaddress.ip_address(parent_scope['startIp']) == netaddr[1] and ipaddress.ip_address(
                    parent_scope['endIp']) == netaddr[-2]:
                return parent_scope['id']
    return "Scope Doesn't Exist"


def get_host_id(host_address, network_address, auth, url):
    """
    Function takes str of ipv4 host address and str of ipv4 networkaddress (CIDR format) with
    auth and url and sends restul call to HPE IMC NMS. Expected return is a str value which
    represents the numerical ID of the target scope

    :param host_address: str describing network address of the target scope in format x.x.x.x
    where x.x.x.x representents the full ipv4 address.  Example:  10.50.0.5 255.255.255.0 would
    be written as 10.50.0.5

    :param network_address: network address of the target scope in format x.x.x.x/yy  where
    x.x.x.x  representents the network address and yy represents the length of the subnet mask.
    Example:  10.50.0.0 255.255.255.0 would be written as 10.50.0.0/24

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str object which contains the numerical ID of the target scope

    :rtype: str
    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.termaccess import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> new_scope = add_ip_scope('10.50.0.1', '10.50.0.254', 'cyoung', 'test group', auth.creds, auth.url)

    >>> add_host_to_segment('10.50.0.5', 'cyoung', 'New Test Host', '10.50.0.0/24', auth.creds, auth.url)

    >>> new_host_id = get_host_id('10.50.0.5', '10.50.0.0/24', auth.creds, auth.url)

    >>> assert type(new_host_id) is str

    """
    scope_id = get_scope_id(network_address, auth, url)
    if scope_id == "Scope Doesn't Exist":
        return scope_id
    all_scope_hosts = get_ip_scope_hosts(auth, url, scopeid=scope_id)
    if len(all_scope_hosts) == 0:
        return "Host Doesn't Exist"
    for host in all_scope_hosts:
        if host['ip'] == host_address:
            return host['id']
        else:
            return "Host Doesn't Exist"
