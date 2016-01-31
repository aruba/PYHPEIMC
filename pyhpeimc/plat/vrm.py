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
from pyhpeimc.plat.device import *


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}




def get_vm_host_info(hostip, auth, url):
    """
    function takes hostId as input to RESTFUL call to HP IMC
    :param hostip: int or string of hostip of Hypervisor host
    :return:list of dictionatires contraining the VM Host information for the target hypervisor
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
    :return:list of dictionatires contraining the VM Host Virtual NIC information for the target hypervisor
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
    :return: list of dictionaries containing the information on the Virtual Machines for the target hypervisor
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
