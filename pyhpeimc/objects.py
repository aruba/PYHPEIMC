#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains class objects for working with the specific types of network
infrastructure equipment in the HPE IMC NMS using the RESTful API. These objects
rely on various other functions from within this library.

"""

# This section imports required libraries
from pyhpeimc.plat.alarms import *
from pyhpeimc.plat.netassets import *
from pyhpeimc.plat.termaccess import *
from pyhpeimc.plat.vlanm import *

from pyhpeimc.auth import HEADERS


# IMC Device Class


class IMCDev:
    """
    imc_dev class takes in the ip_address which is used as the primary key to gather
    the following attributes
    for a device which as been previously discovered in the HP IMC Network Management
    platform.

     Each instance of this class should have the following attributes

     ip: The IP address used to manage the device in HP IMC
     description: returns the description of the device as discovered in HP IMC
     location: returns the location of the device as discovered in HP IMC
     contact: returns the contact of the device as discovered in HP IMC
     type: returns the type of the device as discovered in HP IMC
     name: returns the name of the device as discovered in HP IMC
     status: returns the current alarm status as discovered in HP IMC
     devid: returns the current devid used to internally identify the device
     as discovered in HP IMC
     interfacelist: returns the current list of interfaces for the device as
     discovered in HP IMC
     numinterface: returns a count of the number of interfaces in the interfacelist
     attribute
     vlans: returns the current vlans existing in the device as discovered in HP IMC.
     Device must be supported in the HP IMC Platform VLAN manager module.
     accessinterfaces: returns the device interfaces configured as access interfaces.
     Device must be supported in the HP IMC Platform VLAN manager module.
     trunkinterfaces: returns the device interfaces configured as trunk interfaces.
     Device must be supported in the HP IMC Platform VLAN manager module.
     alarm: returns the current unrecovered alarms as known by HP IMC.
     num alarms: returns a count of the number of alarms as returned by the alarm
     attribute
     serial: returns the network assets, including serial numbers for the device as
     discovered by HP IMC. The device must support the ENTITY MIB ( rfc 4133 ) for
     this value to be returned.
     runconfig: returns the most recent running configuration for the device as known
     by HP IMC. The device must be be supported in the HP IMC platform ICC module.
     startconfig: returns the most recent startup configuration for the device as known
     by HP IMC. The device must be supported in the HP IMC platform ICC module.
     ipmacarp: returns the current device maciparp table as discovered by HP IMC.

     The imc_dev class supports the following methods which can be called upon an instance of
     this class

     getvlans: This method executes the getvlans function on the specific instance of the imc_dev
     object and populates the return into the self.vlans attribute. Devices must be supported in
     the HPE IMC Platform VLAN Manager module
     addvlan: This method executes the addvlan function on the specific instance of the imc_dev
     object. Devices must supported in the HP IMC Platform VLAN Manager module.

     """


    def __init__(self, ip_address, auth, url):
        """
        Function take in input of ipv4 address, auth and url and returns and object of type IMCDev
        :param ip_address: valid IPv4 address
        :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class
        :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass
        :return IMCDev object
        :rtype IMCDev
        """
        self.auth = auth
        self.url = url
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
        self.serials = [({'name': asset['name'], 'serialNum': asset['serialNum']}) for asset in
                         self.assets]
        self.runconfig = get_dev_run_config(self.devid, auth, url)
        self.startconfig = get_dev_start_config(self.devid, auth, url)
        self.ipmacarp = get_ip_mac_arp_list(self.devid, auth, url)

    def getvlans(self):
        """
        Function operates on the IMCDev object and updates the vlans attribute
        :return:
        """
        self.vlans = get_dev_vlans(self.devid, self.auth, self.url)

    def addvlan(self, vlanid, vlan_name, auth, url):
        """
        Function operates on the IMCDev object. Takes input of vlanid (1-4094), str of vlan_name,
        auth and url to execute the create_dev_vlan method on the IMCDev object. Device must be
        supported in the HPE IMC Platform VLAN Manager module.
        :param vlanid: str of VLANId ( valid 1-4094 )
        :param vlan_name: str of vlan_name
        :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class
        :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass
        :return:
        """
        create_dev_vlan(self.devid, vlanid, vlan_name, auth, url)

    def delvlan(self, vlanid, auth, url):
        """
        Function operates on the IMCDev object. Takes input of vlanid (1-4094),
        auth and url to execute the delete_dev_vlans method on the IMCDev object. Device must be
        supported in the HPE IMC Platform VLAN Manager module.
        :param vlanid: str of VLANId ( valid 1-4094 )
        :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class
        :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass
        :return:
        """
        delete_dev_vlans(self.devid, vlanid, auth, url)

    def getipmacarp(self):
        """
        Function operates on the IMCDev object and updates the ipmacarp attribute
        :return:
        """
        self.ipmacarp = get_ip_mac_arp_list(self.devid, self.auth, self.url)


class IMCInterface:
    """
    Class instantiates an object to gather and manipulate attributes and methods of a single
    interface on a single infrastructure device, such as a switch or router.
    """

    def __init__(self, ip_address, ifindex, auth, url):
        self.auth = auth
        self.url = url
        self.ip = get_dev_details(ip_address, self.auth, self.url)['ip']
        self.devid = get_dev_details(ip_address, self.auth, self.url)['id']
        self.ifIndex = get_interface_details(self.devid, ifindex, self.auth, self.url)['ifIndex']
        self.macaddress = get_interface_details(self.devid, ifindex, self.auth, self.url)[
            'phyAddress']
        self.status = get_interface_details(self.devid, ifindex, self.auth, self.url)['statusDesc']
        self.adminstatus = get_interface_details(self.devid, ifindex, self.auth, self.url)[
            'adminStatusDesc']
        self.name = get_interface_details(self.devid, ifindex, self.auth, self.url)['ifDescription']
        self.description = get_interface_details(self.devid, ifindex, self.auth, self.url)[
            'ifAlias']
        self.mtu = get_interface_details(self.devid, ifindex, self.auth, self.url)['mtu']
        self.speed = get_interface_details(self.devid, ifindex, self.auth, self.url)['ifspeed']
        self.accessinterfaces = get_device_access_interfaces(self.devid, self.auth, self.url)
        self.pvid = get_access_interface_vlan(self.ifIndex, self.accessinterfaces, self.auth,
                                               self.url)


# TODO refactor deallocateIp method for human consumption
# TODO Add real_time_locate functionality to nextfreeip method to search IP address before offering

class IPScope:
    """
        Class instantiates an object to gather and manipulate attributes and methods of a IP
        scope as configured in the HPE IMC Platform Terminal Access module.
        """

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

    def allocate_ip(self, hostipaddress, name, description):
        """
        Object method takes in input of hostipaddress, name and description and adds them to the
        parent ip scope.
        :param hostipaddress: str of ipv4 address of the target host ip record
        :param name: str of the name of the owner of the target host ip record
        :param description: str of a description of the target host ip record
        :return:
        """
        add_scope_ip(hostipaddress, name, description, self.id, self.auth, self.url)

    def deallocate_ip(self, hostid):
        """
        Object method takes in input of hostid,removes them from the parent ip scope.
        :param hostid: str of the hostid of  the target host ip record

        :return:
        """
        remove_scope_ip(hostid, self.auth, self.url)

    def gethosts(self):
        """
        Method gets all hosts currently allocated to the target scope and refreashes the self.hosts
        attributes of the object
        :return:
        """
        self.hosts = get_ip_scope_hosts(self.auth, self.url, self.id)

    def nextfreeip(self):
        """
        Method searches for the next free ip address in the scope object and returns it as a str
        value.
        :return:
        """
        allocated_ips = [ipaddress.ip_address(host['ip']) for host in self.hosts]
        for ip in self.netaddr:
            if str(ip).split('.')[-1] == '0':
                continue
            if ip not in allocated_ips:
                return ip

    def addchild(self, startip, endip, name, description):
        """
        Method takes inpur of str startip, str endip, name, and description and adds a child scope.
        The startip and endip MUST be in the IP address range of the parent scope.
        :param startip: str of ipv4 address of the first address in the child scope
        :param endip: str of ipv4 address of the last address in the child scope
        :param name: of the owner of the child scope
        :param description: description of the child scope
        :return:
        """
        add_child_ip_scope(self.auth, self.url, startip, endip, name, description, self.id)
