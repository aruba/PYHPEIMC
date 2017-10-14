# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from pyhpeimc.objects import *
from test_machine import *



# TODO Remarked out failing tests


class TestCreateIMCDev(TestCase):
    """
    Test Case for pyhpeimc objects IMCDev class
    """

    def test_create_IMCDev_type(self):
        """
        test case for creating IMCDev object

        """
        dev1 = IMCDev(CW5_Switch, auth.creds, auth.url)
        self.assertIs(type(dev1), IMCDev)

    def test_create_IMCDev_type(self):
        """
        test case for creating IMCDev object

        """
        dev1 = IMCDev(CW5_Switch, auth.creds, auth.url)
        self.assertIs(type(dev1), IMCDev)

    def test_get_vlans(self):
        """
        test case for getvlans method on IMCDev class object
        :return:
        """
        dev1 = IMCDev(CW5_Switch, auth.creds, auth.url)
        dev1.getvlans()
        self.assertIs(type(dev1.vlans), list)

    def test_add_vlan(self):
        """
        test case for add_vlans method on IMCDev object
        :return:
        """
        dev1 = IMCDev(CW5_Switch, auth.creds, auth.url)
        dev1.delvlan('500')
        dev1.addvlan('500','testvlan')
        dev1.getvlans()
        vlans = [vlan['vlanId'] for vlan in dev1.vlans]
        self.assertIn('500',vlans)
        dev1.delvlan('500')

    def test_del_vlan(self):
        """
        test case for del_vlan method on IMCDev object
        :return:
        """
        dev1 = IMCDev(CW5_Switch, auth.creds, auth.url)
        dev1.addvlan('500', 'testvlan')
        dev1.delvlan('500')
        dev1.getvlans()
        vlans = [vlan['vlanId'] for vlan in dev1.vlans]
        self.assertNotIn('500', vlans)

    def test_get_ipmacarp(self):
        """
        test case for get_ipmacarp method on IMCDev object
        :return:
        """
        dev1 = IMCDev(CW5_Switch, auth.creds, auth.url)
        dev1.getipmacarp()
        self.assertIs(type(dev1.ipmacarp), list)


class TestIMCInterface(TestCase):
    """
    Test Case for pyhpeimc objects IMCInterface class objects
    """

    def test_create_IMCDev_type(self):
        """
        test case for creating IMCInterface object

        """
        Interface1 = IMCInterface(CW5_Switch,CW5_Interface, auth.creds, auth.url)
        self.assertIs(type(Interface1), IMCInterface)

    def test_down_interface(self):
        """
        test case for down method on IMCInterface object
        :return:
        """
        Interface1 = IMCInterface(CW5_Switch, CW5_Interface, auth.creds, auth.url)
        Interface1.down()
        self.assertEquals(Interface1.adminstatus, 'Down' )

    def test_up_interface(self):
        """
        test case for up method on IMCInterface object
        :return:
        """
        Interface1 = IMCInterface(CW5_Switch, CW5_Interface, auth.creds, auth.url)
        Interface1.up()
        self.assertEquals(Interface1.adminstatus, 'Up')


class TestIPScope(TestCase):
    """
    Test Case for pyhpeimc objects IPScope class
    """

    def test_create_IPScope_type(self):
        """
        test case for creating IMCInterface object

        """
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        Scope1 = IPScope(term_access_ipam_network_scope, auth.creds, auth.url)
        self.assertIs(type(Scope1), IPScope)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)

    def test_get_hosts(self):
        """
        test case for get_hosts method of IPScope class object
        :return:
        """
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        Scope1 = IPScope(term_access_ipam_network_scope, auth.creds, auth.url)
        Scope1.gethosts()
        self.assertIs(type(Scope1.hosts), list)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)


    def test_allocate_host_ip(self):
        """
        test case for allocate_ip method of IPScope class object
        :return:
        """
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        Scope1 = IPScope(term_access_ipam_network_scope, auth.creds, auth.url)
        Scope1.allocate_ip(term_access_ipam_host,'test_host', 'my_test')
        Scope1.gethosts()
        hosts = [ host['ip'] for host in Scope1.hosts]
        self.assertIn(term_access_ipam_host, hosts)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)

    def test_deallocate_host_ip(self):
        """
        test case for allocate_ip method of IPScope class object
        :return:
        """
        new_scope = add_ip_scope('cyoung', 'test group', auth.creds, auth.url,
                                 network_address=term_access_ipam_network_scope)
        Scope1 = IPScope(term_access_ipam_network_scope, auth.creds, auth.url)
        Scope1.allocate_ip(term_access_ipam_host, 'test_host', 'my_test')
        Scope1.gethosts()
        hosts = [host['ip'] for host in Scope1.hosts]
        self.assertIn(term_access_ipam_host, hosts)
        Scope1.deallocate_ip(term_access_ipam_host)
        Scope1.gethosts()
        if 'ip' in Scope1.hosts[0]:
            hosts = [host['ip'] for host in Scope1.hosts]
            self.assertNotIn(term_access_ipam_host, hosts)
        delete_ip_scope(term_access_ipam_network_scope, auth.creds, auth.url)


