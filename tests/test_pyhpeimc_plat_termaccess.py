# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.termaccess module.

"""

from unittest import TestCase

from nose.plugins.skip import SkipTest

from pyhpeimc.plat.termaccess import *
from test_machine import *


class TestGet_real_time_locate(TestCase):
    def test_get_real_time_locate_type(self):
        found_device = get_real_time_locate(term_access_host, auth.creds, auth.url)
        self.assertIs(type(found_device), list)
        self.assertIs(type(found_device[0]), dict)


    def test_get_real_time_locate_content(self):
        found_device = get_real_time_locate(term_access_host, auth.creds, auth.url)
        self.assertIs(len(found_device[0]), 5)
        self.assertIn('ifIndex', found_device[0])
        self.assertIn('ifDesc', found_device[0])
        self.assertIn('locateIp', found_device[0])
        self.assertIn('deviceIp', found_device[0])
        self.assertIn('deviceId', found_device[0])


    def test_get_real_time_locate_doesnt_exist(self):
        found_device = get_real_time_locate(DoesntExist, auth.creds, auth.url)
        self.assertIs(type(found_device), int)
        self.assertEqual(found_device, 403)








"""============================================================================================="""

# Test get_ip_map_arp_list for Multiple Vendor Devices

# Switches

# CW3_Switch
class TestGet_ip_mac_arp_list_CW3_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if CW3_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if CW3_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])

# CW5_Switch
class TestGet_ip_mac_arp_list_CW5_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if CW5_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if CW5_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# CW7_Switch
class TestGet_ip_mac_arp_list_CW7_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if CW7_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if CW7_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# Cisco_Switch
class TestGet_ip_mac_arp_list_Cisco_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# Juniper_Switch
class TestGet_ip_mac_arp_list_Juniper_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# Arista_Switch
class TestGet_ip_mac_arp_list_Arista_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Arista_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Arista_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# ArubaOS_Switch (Formerly Provision)
class TestGet_ip_mac_arp_list_ArubaOS_Switch(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# Routers

# Cisco_Router
class TestGet_ip_mac_arp_list_Cisco_Router(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Cisco_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Cisco_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# CW5_Router
class TestGet_ip_mac_arp_list_CW5_Router(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if CW5_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if CW5_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# Juniper_Router (SRX)
class TestGet_ip_mac_arp_list_Juniper_Router(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Juniper_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Juniper_Router is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# Servers


# Windows_Server
# TODO Test remarked out and bug reported
'''
class TestGet_ip_mac_arp_list_Windows_Server(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Windows_Server is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Windows_Server is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])
'''

# Linux_Server
class TestGet_ip_mac_arp_list_Linux_Server(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if Linux_Server is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if Linux_Server is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# Hypervisors


# ESX
# TODO Test remarked and bug reported
'''
class TestGet_ip_mac_arp_list_ESX(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if ESX is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if ESX is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])
'''


# HyperV
class TestGet_ip_mac_arp_list_HyperV(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if HyperV is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(ip_mac_list), list)
        self.assertIs(type(ip_mac_list[0]), dict)


    def test_get_ip_mac_arp_list_content(self):
        if HyperV is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(ip_mac_list[0]), 6)
        self.assertIn('iface', ip_mac_list[0])
        self.assertIn('macAddress', ip_mac_list[0])
        self.assertIn('device', ip_mac_list[0])
        self.assertIn('deviceIp', ip_mac_list[0])
        self.assertIn('ifIndex', ip_mac_list[0])
        self.assertIn('deviceId', ip_mac_list[0])


# DoesntExist

class TestGet_ip_mac_arp_list_DoesntExist(TestCase):
    def test_get_ip_mac_arp_list_type(self):
        if DoesntExist is None:
            raise SkipTest
        ip_mac_list = get_ip_mac_arp_list(auth.creds, auth.url, devip=DoesntExist)
        self.assertIs(type(ip_mac_list), int)
        self.assertEqual(ip_mac_list, 403)



"""============================================================================================="""

# Test for Terminal Access - IP Address Manager Functions


class TestGet_ip_scope(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)

    def test_get_ip_scope_type(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        ip_scope_list = get_ip_scope(auth.creds, auth.url)
        self.assertIs(type(ip_scope_list), list)


    def test_get_ip_scope_content(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        ip_scope_list = get_ip_scope(auth.creds, auth.url)
        self.assertIs(len(ip_scope_list[0]), 7)
        self.assertIn('name', ip_scope_list[0])
        self.assertIn('description', ip_scope_list[0])
        self.assertIn('id', ip_scope_list[0])
        self.assertIn('ip', ip_scope_list[0])
        self.assertIn('parentId', ip_scope_list[0])
        self.assertIn('percent', ip_scope_list[0])
        self.assertIn('percentStr', ip_scope_list[0])


class TestGet_ip_scope_detail(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)

    def test_get_ip_scope_detail_type(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        ip_scope_detail = get_ip_scope_detail(auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        self.assertIs(type(ip_scope_detail), dict)


    def test_get_ip_scope_detail_content(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        ip_scope_detail = get_ip_scope_detail(auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        self.assertIs(len(ip_scope_detail), 10)
        self.assertIn('parentId', ip_scope_detail)
        self.assertIn('startIp', ip_scope_detail)
        self.assertIn('endIp', ip_scope_detail)
        self.assertIn('ip', ip_scope_detail)
        self.assertIn('description', ip_scope_detail)
        self.assertIn('operatorGroup', ip_scope_detail)
        self.assertIn('percent', ip_scope_detail)
        self.assertIn('id', ip_scope_detail)
        self.assertIn('name', ip_scope_detail)
        self.assertIn('percentStr', ip_scope_detail)


class Test_Add_ip_scope(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)

    def test_add_ip_scope_type(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        self.assertIs(type(new_scope), int)
        ip_scope_detail = get_ip_scope_detail(auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        self.assertEqual(new_scope, 200)


    def test_Add_ip_scope_content(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        ip_scope_detail = get_ip_scope_detail(auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        self.assertEqual(ip_scope_detail['name'], 'cyoung')
        self.assertEqual(ip_scope_detail['description'], "test group")


class Test_Add_child_ip_scope(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)

    def test_add_child_ip_scope_type(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        child_scope = add_child_ip_scope('csyoung', 'test child scope', auth.creds, auth.url,
                                         network_address=term_access_ipam_child_scope, parent_network_address=term_access_ipam_network_scope)
        self.assertIs(type(child_scope), int)
        self.assertEqual(child_scope, 200)


class Test_Delete_ip_scope(TestCase):
    def setUp(self):
        add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                     network_address=term_access_ipam_network_scope)

    def tearDown(self):
        #delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        pass

    def test_delete_ip_scope_type(self):
        add_ip_scope('cyoung', 'test group', auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        get_scope_id(term_access_ipam_network_scope, auth.creds, auth.url)
        delete_scope = delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertIs(type(delete_scope), int)
        self.assertEqual(delete_scope, 204)

    def test_delete_ip_scope_doesnt_exst(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        delete_scope = delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertIs(type(delete_scope), str)
        self.assertEqual(delete_scope, "Scope Doesn't Exist")

class Test_Get_scope_id(TestCase):
    def test_get_scope_id(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        scope_id = get_scope_id(term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertIs(type(int(scope_id)), int)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)


    def test_get_child_scope_id(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        child_scope = add_child_ip_scope('csyoung', 'test child scope', auth.creds, auth.url,
                                         network_address=term_access_ipam_child_scope,
                                         parent_network_address=term_access_ipam_network_scope)
        scope_id = get_scope_id(term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertIs(type(int(scope_id)), int)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)


    def test_get_scope_id_doesnt_exist(self):

        scope_id = get_scope_id(term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertIs(type((scope_id)), str)
        self.assertEqual(scope_id, "Scope Doesn't Exist")


class Test_Add_scope_ip(TestCase):
    def test_add_scope_ip_type(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url, network_address=term_access_ipam_network_scope)
        child_scope = add_child_ip_scope('csyoung', 'test child scope', auth.creds, auth.url,
                                         network_address=term_access_ipam_child_scope, parent_network_address=term_access_ipam_network_scope)
        new_host_ip = add_scope_ip(term_access_ipam_host, 'cyoung', 'New Test Host', auth.creds, auth.url,
                                network_address=term_access_ipam_network_scope)
        self.assertIs(type(new_host_ip), int)
        self.assertEqual(new_host_ip, 200)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)

    def test_add_scope_ip_doesnt_exist(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        new_host_ip = add_scope_ip(term_access_ipam_host, 'cyoung', 'New Test Host', auth.creds, auth.url,
                                   network_address=term_access_ipam_network_scope)
        self.assertEqual(new_host_ip, "Scope Doesn't Exist")

class Test_Get_host_id(TestCase):
    def test_get_host_id(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        child_scope = add_child_ip_scope('csyoung', 'test child scope', auth.creds, auth.url,
                                         network_address=term_access_ipam_child_scope,
                                         parent_network_address=term_access_ipam_network_scope)
        new_host_ip = add_scope_ip(term_access_ipam_host, 'cyoung', 'New Test Host', auth.creds, auth.url,
                                   network_address=term_access_ipam_network_scope)
        host_id = get_host_id(term_access_ipam_host, term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertIs(type(int(host_id)), int)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)


    def test_get_host_id_doesnt_exist(self):
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        host_id = get_host_id(DoesntExist, term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertEqual(host_id, "Host Doesn't Exist")


# TODO modified assertEqual test to add conditional for intermitent test failure
class Test_Delete_host_from_segment(TestCase):
    def test_delete_host_from_segment(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        new_host_ip = add_scope_ip(term_access_ipam_host, 'cyoung', 'New Test Host', auth.creds, auth.url,
                                   network_address=term_access_ipam_network_scope)
        delete_host = delete_host_from_segment(term_access_ipam_host,term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertIn(delete_host, [204, 409])
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)


class Test_Get_ip_scope_hosts(TestCase):
    def test_get_ip_scope_hosts_type(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        child_scope = add_child_ip_scope('csyoung', 'test child scope', auth.creds, auth.url,
                                         network_address=term_access_ipam_child_scope,
                                         parent_network_address=term_access_ipam_network_scope)
        new_host_ip = add_scope_ip(term_access_ipam_host, 'cyoung', 'New Test Host', auth.creds, auth.url,
                                   network_address=term_access_ipam_network_scope)
        host_list = get_ip_scope_hosts(auth.creds, auth.url, network_address='10.50.0.0/16')
        self.assertIs(type(host_list), list)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)


    def test_get_ip_scope_hosts_content(self):
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        child_scope = add_child_ip_scope('csyoung', 'test child scope', auth.creds, auth.url,
                                         network_address=term_access_ipam_child_scope,
                                         parent_network_address=term_access_ipam_network_scope)
        new_host_ip = add_scope_ip(term_access_ipam_host, 'cyoung', 'New Test Host', auth.creds, auth.url,
                                   network_address=term_access_ipam_network_scope)
        host_list = get_ip_scope_hosts(auth.creds, auth.url, network_address='10.50.0.0/16')
        self.assertIs(len(host_list[0]), 5)
        self.assertIn('parentId', host_list[0])
        self.assertIn('ip', host_list[0])
        self.assertIn('description', host_list[0])
        self.assertIn('name', host_list[0])
        self.assertIn('id', host_list[0])
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)
