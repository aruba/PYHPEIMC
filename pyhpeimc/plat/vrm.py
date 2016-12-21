#!/usr/bin/env python3
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the Virtual Resource Manager capabilities of the HPE IMC NMS platform
using the RESTful API

"""



# This section imports required libraries
import json
import requests
from pyhpeimc.plat.device import *


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}




def get_vm_host_info(hostip, auth, url):
    """
    function takes hostId as input to RESTFUL call to HP IMC

    :param hostip: int or string of hostip of Hypervisor host

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: Dictionary contraining the information for the target VM host

    :rtype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vrm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> host_info = get_vm_host_info('10.101.0.6', auth.creds, auth.url)

    >>> assert type(host_info) is dict

    >>> assert len(host_info) == 10

    >>> assert 'cpuFeg' in host_info

    >>> assert 'cpuNum' in host_info

    >>> assert 'devId' in host_info

    >>> assert 'devIp' in host_info

    >>> assert 'diskSize' in host_info

    >>> assert 'memory' in host_info

    >>> assert 'parentDevId' in host_info

    >>> assert 'porductFlag' in host_info

    >>> assert 'serverName' in host_info

    >>> assert 'vendor' in host_info

    """
    hostId = get_dev_details(hostip, auth, url)['id']
    get_vm_host_info_url = "/imcrs/vrm/host?hostId=" + str(hostId)
    f_url = url + get_vm_host_info_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)
        elif r.status_code == 204:
            print("Device is not a supported Hypervisor")
            return "Device is not a supported Hypervisor"
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_vm_host_info: An Error has occured"

def get_vm_host_vnic(hostip, auth, url):
    """
    function takes hostId as input to RESTFUL call to HP IMC

    :param hostip: int or string of hostip of Hypervisor host

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents a single NIC on the target host

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vrm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> host_vnic = get_vm_host_vnic('10.101.0.6', auth.creds, auth.url)

    >>> assert type(host_vnic) is list

    >>> assert (len(host_vnic[0])) is 6

    >>> assert 'ip' in host_vnic[0]

    >>> assert 'mask' in host_vnic[0]

    >>> assert 'nicName' in host_vnic[0]

    >>> assert 'serverDevId' in host_vnic[0]

    >>> assert 'vSwitchName' in host_vnic[0]

    >>> assert 'vSwtichKey' in host_vnic[0]


    """
    hostId = get_dev_details(hostip, auth, url)['id']
    get_vm_host_vnic_url = "/imcrs/vrm/host/vnic?hostDevId=" + str(hostId)
    f_url = url + get_vm_host_vnic_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['Nic']
        elif r.status_code == 204:
            print("Device is not a supported Hypervisor")
            return "Device is not a supported Hypervisor"
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_vm_host_info: An Error has occured"

def get_host_vms(hostip, auth, url):
    """
    function takes hostId as input to RESTFUL call to HP IMC

    :param hostId: int or string of HostId of Hypervisor host

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element of the list represents a single virtual machine which is currently
    located on the target host.

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.vrm import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> host_vms = get_host_vms('10.101.0.6', auth.creds, auth.url)

    >>> assert type(host_vms) is list

    >>> assert len(host_vms[0]) == 12

    >>> assert 'coresPerCpu' in host_vms[0]

    >>> assert 'cpu' in host_vms[0]

    >>> assert 'memory' in host_vms[0]

    >>> assert 'osDesc' in host_vms[0]

    >>> assert 'parentServerId' in host_vms[0]

    >>> assert 'porductFlag' in host_vms[0]

    >>> assert 'vmDevId' in host_vms[0]

    >>> assert 'vmIP' in host_vms[0]

    >>> assert 'vmMask' in host_vms[0]

    >>> assert 'vmName' in host_vms[0]

    >>> assert 'vmTools' in host_vms[0]

    """
    hostId = get_dev_details(hostip, auth, url)['id']
    get_host_info_url = "/imcrs/vrm/host/vm?hostId=" + str(hostId)
    f_url = url + get_host_info_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            if len(json.loads(r.text)) > 1:
                return json.loads(r.text)['vmDevice']
            else:
                return "Device is not a supported Hypervisor"
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_host_vms: An Error has occured"
