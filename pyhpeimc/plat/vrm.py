#!/usr/bin/env python3
# author: @netmanchris



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

    >>>get_vm_host_info('10.101.0.6', auth.creds, auth.url)
    {'cpuFeg': '2297',
 'cpuNum': '40',
 'devId': '76',
 'devIp': '10.101.0.6',
 'diskSize': '0',
 'memory': '114559',
 'parentDevId': '56',
 'porductFlag': '0',
 'serverName': 'esx1.lab.local',
 'vendor': 'HP'}


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

    >>> get_vm_host_vnic('10.101.0.6', auth.creds, auth.url)
    [{'ip': '10.101.0.6',
  'mask': '255.255.255.0',
  'nicName': 'vmk0',
  'serverDevId': '76',
  'vSwitchName': 'vSwitch0',
  'vSwtichKey': 'key-vim.host.VirtualSwitch-vSwitch0'},
 {'ip': '10.101.0.123',
  'mask': '255.255.255.0',
  'nicName': 'vmk1',
  'serverDevId': '76',
  'vSwitchName': 'vSwitch0',
  'vSwtichKey': 'key-vim.host.VirtualSwitch-vSwitch0'},
 {'ip': '',
  'mask': '',
  'nicName': 'vmnic0',
  'serverDevId': '76',
  'vSwitchName': 'vSwitch0',
  'vSwtichKey': 'key-vim.host.VirtualSwitch-vSwitch0'},
 {'ip': '',
  'mask': '',
  'nicName': 'vmnic1',
  'serverDevId': '76',
  'vSwtichKey': ''},
 {'ip': '',
  'mask': '',
  'nicName': 'vmnic2',
  'serverDevId': '76',
  'vSwtichKey': ''},
 {'ip': '',
  'mask': '',
  'nicName': 'vmnic3',
  'serverDevId': '76',
  'vSwtichKey': ''},
 {'ip': '',
  'mask': '',
  'nicName': 'vmnic4',
  'serverDevId': '76',
  'vSwtichKey': ''},
 {'ip': '',
  'mask': '',
  'nicName': 'vmnic5',
  'serverDevId': '76',
  'vSwtichKey': ''}]


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

    >>>get_host_vms('10.101.0.6', auth.creds, auth.url)
[{'coresPerCpu': '1',
  'cpu': '2',
  'memory': '8192',
  'osDesc': 'SUSE Linux Enterprise 11 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '2',
  'vmDevId': '56',
  'vmIP': '10.101.0.5',
  'vmMask': ' ',
  'vmName': 'vcenter6',
  'vmTools': '2'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '4096',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '2',
  'vmDevId': '57',
  'vmIP': '10.101.0.20',
  'vmMask': ' ',
  'vmName': '2016 Microsoft Server 2012R2 AD + DHCP 10.101.0.20',
  'vmTools': '2'},
 {'coresPerCpu': '4',
  'cpu': '1',
  'memory': '12288',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '2',
  'vmDevId': '67',
  'vmIP': '10.101.0.203',
  'vmMask': ' ',
  'vmName': 'HPE IMC 7.2 Jan 2016 10.101.0.203',
  'vmTools': '2'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '4096',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '2',
  'vmDevId': '71',
  'vmIP': '10.101.0.202',
  'vmMask': ' ',
  'vmName': 'HP IMC 7.1 June 2015 10.101.0.202',
  'vmTools': '2'},
 {'coresPerCpu': '1',
  'cpu': '2',
  'memory': '4096',
  'osDesc': 'Other (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '3',
  'vmDevId': '147',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'F5 BIG-IP VE 11.3.0.2806.0',
  'vmTools': '14'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '4096',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '3',
  'vmDevId': '148',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'RSM 7.0 10.101.0.191',
  'vmTools': '14'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '4096',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '3',
  'vmDevId': '149',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'RSM 7.2 10.101.0.193',
  'vmTools': '14'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '6144',
  'osDesc': 'CentOS 4/5/6 (32-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '3',
  'vmDevId': '151',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'HP vSMS new',
  'vmTools': '14'},
 {'coresPerCpu': '1',
  'cpu': '2',
  'memory': '2816',
  'osDesc': 'Other (32-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '32769',
  'vmDevId': '152',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'HP IMC UCHM Demo (2)',
  'vmTools': '14'},
 {'coresPerCpu': '2',
  'cpu': '1',
  'memory': '8192',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '2',
  'vmDevId': '153',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': '2014 Home IMC 10.3.10.220',
  'vmTools': '12'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '4096',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '3',
  'vmDevId': '154',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'Solarwinds Orion',
  'vmTools': '12'},
 {'coresPerCpu': '1',
  'cpu': '2',
  'memory': '4096',
  'osDesc': 'Ubuntu Linux (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '32769',
  'vmDevId': '155',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'CiscoONEPK_AIO',
  'vmTools': '12'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '4096',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '32769',
  'vmDevId': '156',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'HP IMC 5.2 10.101.0.200',
  'vmTools': '14'},
 {'coresPerCpu': '1',
  'cpu': '2',
  'memory': '8192',
  'osDesc': 'SUSE Linux Enterprise 11 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '3',
  'vmDevId': '157',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'vCenter Server Appliance 2014 10.101.0.5',
  'vmTools': '14'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '4096',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '3',
  'vmDevId': '158',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'vCenter Windows Sept 2015 10.101.0.9',
  'vmTools': '14'},
 {'coresPerCpu': '1',
  'cpu': '2',
  'memory': '8192',
  'osDesc': 'SUSE Linux Enterprise 11 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '3',
  'vmDevId': '159',
  'vmIP': ' ',
  'vmMask': ' ',
  'vmName': 'VMware vCenter Server Appliance 2016 10.101.0.5',
  'vmTools': '14'},
 {'coresPerCpu': '1',
  'cpu': '1',
  'memory': '4096',
  'osDesc': 'Microsoft Windows Server 2012 (64-bit)',
  'parentServerId': '76',
  'porductFlag': '0',
  'powerState': '2',
  'vmDevId': '229',
  'vmIP': '10.101.0.201',
  'vmMask': ' ',
  'vmName': 'HP IMC 7.0 10.101.0.201',
  'vmTools': '2'}]

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
