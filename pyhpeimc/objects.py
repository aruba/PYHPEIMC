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
import requests
import json
from pyhpeimc.plat.device import *
from pyhpeimc.plat.vlanm import *
from pyhpeimc.plat.termaccess import *
from pyhpeimc.plat.netassets import *
from pyhpeimc.plat.alarms import *
from requests.auth import HTTPDigestAuth


headers = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

# IMC Device Class

class IMCDev:
    """
    imc_dev class takes in the ip_address which is used as the primary key to gather the following attributes
         for a device which as been previously discovered in the HP IMC Network Management platform.
         Each instance of this class should have the following attributes

         ip: The IP address used to manage the device in HP IMC
         description: returns the description of the device as discovered in HP IMC
         location: returns the location of the device as discovered in HP IMC
         contact: returns the contact of the device as discovered in HP IMC
         type: returns the type of the device as discovered in HP IMC
         name: returns the name of the device as discovered in HP IMC
         status: returns the current alarm status as discovered in HP IMC
         devid: returns the current devid used to internally identify the device as discovered in HP IMC
         interfacelist: returns the current list of interfaces for the device as discovered in HP IMC
         numinterface: returns a count of the number of interfaces in the interfacelist attribute
         vlans: returns the current vlans existing in the device as discovered in HP IMC. Device must be supported in the
                HP IMC Platform VLAN manager module.
         accessinterfaces: returns the device interfaces configured as access interfaces. Device must be supported in the
                HP IMC Platform VLAN manager module.
         trunkinterfaces: returns the device interfaces configured as trunk interfaces. Device must be supported in the
                HP IMC Platform VLAN manager module.
         alarm: returns the current unrecovered alarms as known by HP IMC.
         num alarms: returns a count of the number of alarms as returned by the alarm attribute
         serial: returns the network assets, including serial numbers for the device as discovered by HP IMC. The device
                must support the ENTITY MIB ( rfc 4133 ) for this value to be returned.
         runconfig: returns the most recent running configuration for the device as known by HP IMC. The device must be
                be supported in the HP IMC platform ICC module.
         startconfig: returns the most recent startup configuration for the device as known by HP IMC. The device must be
                be supported in the HP IMC platform ICC module.
         ipmacarp: returns the current device maciparp table as discovered by HP IMC.

         The imc_dev class supports the following methods which can be called upon an instance of this class

         addvlan: This method executes the addvlan function on the specific instance of the imc_dev object. Devices must
                  supported in the HP IMC Platform VLAN Manager module.

         """

    def __init__(self, ip_address, auth, url):
        self.ip = get_dev_details(ip_address, auth, url)['ip']
        self.description = get_dev_details(ip_address, auth, url)['sysDescription']
        self.location = get_dev_details(ip_address, auth, url)['location']
        self.contact = get_dev_details(ip_address, auth, url)['contact']
        self.type = get_dev_details(ip_address, auth, url)['typeName']
        self.name = get_dev_details(ip_address, auth, url)['sysName']
        self.status = get_dev_details(ip_address, auth, url)['statusDesc']
        self.devid = get_dev_details(ip_address, auth, url)['id']
        self.interfacelist = get_dev_interface(self.devid, auth, url)
        self.numinterface = len(get_dev_interface(self.devid, auth, url))
        self.vlans = get_dev_vlans(self.devid, auth, url)
        self.accessinterfaces = get_device_access_interfaces(self.devid, auth, url)
        self.trunkinterfaces = get_trunk_interfaces(self.devid, auth, url)
        self.alarm = get_dev_alarms(self.devid, auth, url)
        self.numalarm = len(get_dev_alarms(self.devid, auth, url))
        self.assets = get_dev_asset_details(self.ip, auth, url)
        self.serials = [({'name' : asset['name'], 'serialNum': asset['serialNum']}) for asset in self.assets]
        self.runconfig = get_dev_run_config(self.devid, auth, url)
        self.startconfig = get_dev_start_config(self.devid, auth, url)
        self.ipmacarp = get_ip_mac_arp_list(self.devid, auth, url)
        self.auth = auth
        self.url = url

    def getvlans(self):
        self.vlans = get_dev_vlans(self.devid, self.auth, self.url)

    def addvlan(self, vlanid, vlan_name,auth, url):
        create_dev_vlan(self.devid, vlanid, vlan_name, auth, url)

    def delvlan(self, vlanid, auth, url):
        delete_dev_vlans(self.devid, vlanid, auth, url)

    def getipmacarp(self):
        self.ipmacarp = get_ip_mac_arp_list(self.devid, auth, url)


class IMCInterface:
    def __init__(self, ip_address, ifIndex, auth, url):
        self.ip = get_dev_details(ip_address,auth, url)['ip']
        self.devid = get_dev_details(ip_address,auth, url)['id']
        self.ifIndex = get_interface_details(self.devid, ifIndex,auth, url)['ifIndex']
        self.macaddress = get_interface_details(self.devid, ifIndex,auth, url)['phyAddress']
        self.status = get_interface_details(self.devid, ifIndex,auth, url)['statusDesc']
        self.adminstatus = get_interface_details(self.devid, ifIndex,auth, url)['adminStatusDesc']
        self.name = get_interface_details(self.devid, ifIndex,auth, url)['ifDescription']
        self.description = get_interface_details(self.devid, ifIndex,auth, url)['ifAlias']
        self.mtu = get_interface_details(self.devid, ifIndex,auth, url)['mtu']
        self.speed = get_interface_details(self.devid, ifIndex,auth, url)['ifspeed']
        self.accessinterfaces = get_device_access_interfaces(self.devid,auth, url)
        self.pvid = get_access_interface_vlan(self.ifIndex, self.accessinterfaces,auth, url)
        self.auth = auth
        self.url = url


class IPScope:
    def __init__(self, netaddr, auth, url):
        self.id = get_scope_id(netaddr, auth, url)
        self.details = get_ip_scope_detail(auth, url, self.id)
        self.hosts = get_ip_scope_hosts(auth, url, self.id)
        self.auth = auth
        self.url = url
        self.netaddr = ipaddress.ip_network(netaddr)
        self.startip = get_ip_scope_detail(auth, url, self.id)['startIp']
        self.endip = get_ip_scope_detail(auth, url, self.id)['endIp']
        if 'assignedIpScope' in self.details:
            self.child = get_ip_scope_detail(auth, url, self.id)['assignedIpScope']

    def allocateIp(self, ipaddress, name, description):
        add_scope_ip(ipaddress, name, description, self.id, self.auth, self.url)

    def deallocateIp(self, hostid):
        remove_scope_ip( hostid, self.auth, self.url)

    def gethosts(self):
        self.hosts = get_ip_scope_hosts(self.auth, self.url, self.id)


    def nextfreeip(self):
        allocated_ips = [ ipaddress.ip_address(host['ip']) for host in self.hosts]
        for ip in self.netaddr:
            if str(ip).split('.')[-1] == '0':
                continue
            if ip not in allocated_ips:
                return ip

    def addchild(self, startIp, endIp, name, description):
        add_child_ip_scope(self.auth, self.url,startIp, endIp, name, description,self.id)






