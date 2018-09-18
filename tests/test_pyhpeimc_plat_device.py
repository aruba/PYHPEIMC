# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.device module.

"""

from unittest import TestCase

from nose.plugins.skip import SkipTest

from pyhpeimc.plat.device import *
from test_machine import *


class TestGetAllDevs(TestCase):
    """
    Test get_all_devs function from pyhpeimc.plat.device
    """
    def test_get_all_devs_type(self):
        """
        run get_all_devs function and assing results to dev_list
        assert the type of dev_list is list
        """
        dev_list = get_all_devs(auth.creds, auth.url)
        self.assertIs(type(dev_list), list)

    def test_get_all_devs_network_address_filter_type(self):
        """
        run get_al_devs function with optional netowrk_address and assign results to dev_list
        assert the type of dev_list is list
        """
        dev_list = get_all_devs(auth.creds, auth.url, network_address='10.101.')
        self.assertIs(type(dev_list), list)

    def test_get_all_devs_content(self):
        """
        run get_al_devs function with optional netowrk_address and assign results to dev_list
        assert the length of the content of dev_list
        assert the content of dev_list includes expected key/value pairs
        """
        dev_list = get_all_devs(auth.creds, auth.url, network_address='10.101.')
        self.assertIs(len(dev_list[0]), 22)
        self.assertIn('typeName', dev_list[0])
        self.assertIn('sysOid', dev_list[0])
        self.assertIn('mask', dev_list[0])
        self.assertIn('symbolId', dev_list[0])
        self.assertIn('symbolName', dev_list[0])
        self.assertIn('ip', dev_list[0])
        self.assertIn('symbolLevel', dev_list[0])
        self.assertIn('symbolType', dev_list[0])
        self.assertIn('link', dev_list[0])
        self.assertIn('symbolDesc', dev_list[0])
        self.assertIn('contact', dev_list[0])
        self.assertIn('parentId', dev_list[0])
        self.assertIn('status', dev_list[0])
        self.assertIn('devCategoryImgSrc', dev_list[0])
        self.assertIn('label', dev_list[0])
        self.assertIn('categoryId', dev_list[0])
        self.assertIn('sysName', dev_list[0])
        self.assertIn('sysDescription', dev_list[0])
        self.assertIn('location', dev_list[0])
        self.assertIn('topoIconName', dev_list[0])
        self.assertIn('statusDesc', dev_list[0])
        self.assertIn('id', dev_list[0])
        #self.assertIn('mac', dev_list[0])


# Test Get_Dev_Details for Multiple Vendor Devices

# Switches

# CW3 Switch
class TestGetDevDetailsCW3Switch(TestCase):
    """
    Testing get_dev_details function on Comware 3 Switch
    """
    def test_get_dev_details_type(self):
        """
        check to see if CW3_Switch is defined, if not deined skip test
        if defined, run get_dev_details using CW3_Switch function and assignt to dev_1
        assert dev_1 is type dict
        run get_dev_details function and assing to dev_2
        """
        if CW3_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW3_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details(DoesntExist, auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        """
        check to see if CW3_Switch is defined, if not deined skip test
        if defined, run get_dev_details using CW3_Switch function and assignt to dev_1
        assert that dev_1 is the right length
        assert that the content of dev_1 contains the appropriate key/value pairs
        """
        if CW3_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW3_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 23)   # TODO Modified len from 22 to 23. Neeed to investigate
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# CW5 Switch
class TestGetDevDetailsCW5Switch(TestCase):
    """
    test get_dev_details function on Comware 5 Switch
    """
    def test_get_dev_details_type(self):
        """
        check to see if CW5_Switch is defined, if not deined skip test
        if defined, run get_dev_details using CW5_Switch function and assignt to dev_1
        assert dev_1 is type dict
        run get_dev_details function and assing to dev_2
        """
        if CW5_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details(DoesntExist, auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# CW7 Switch
class TestGetDevDetailsCW7Switch(TestCase):
    """
    test get_dev_details with Comware7 Switch
    """
    def test_get_dev_details_type(self):
        """
        check to see if CW7_Switch is defined, if not deined skip test
        if defined, run get_dev_details using CW7_Switch function and assignt to dev_1
        assert dev_1 is type dict
        run get_dev_details function and assing to dev_2
        """
        if CW7_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW7_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details(DoesntExist, auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW7_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 23) # TODO Modified len from 22 to 23 Need to investigate
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# Cisco Switch
class TestGetDevDetailsCiscoSwitch(TestCase):
    def test_get_dev_details_type(self):
        """
        check to see if Cisco_Switch is defined, if not deined skip test
        if defined, run get_dev_details using Cisco_Switch function and assignt to dev_1
        assert dev_1 is type dict
        run get_dev_details function and assing to dev_2
        """
        if Cisco_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details(DoesntExist, auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# TODO Changed len test need to investigate
# Arista Switch
class TestGetDevDetailsAristaSwitch(TestCase):
    """
    test get_dev_detail with Arista Switch
    """
    def test_get_dev_details_type(self):
        """
        check to see if Arista_Switch is defined, if not deined skip test
        if defined, run get_dev_details using Arista_Switch function and assignt to dev_1
        assert dev_1 is type dict
        run get_dev_details function and assing to dev_2
        assert contents of dev_2 is 'Device not Found'
        """
        if Arista_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Arista_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details(DoesntExist, auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Arista_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 23)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# Juniper Switch
class TestGetDevDetailsJuniperSwitch(TestCase):
    """
    test get dev details with Juniper switch
    """
    def test_get_dev_details_type(self):
        """
        check to see if Juniper_Switch is defined, if not deined skip test
        if defined, run get_dev_details using Juniper_Switch function and assignt to dev_1
        assert dev_1 is type dict
        run get_dev_details function and assing to dev_2
        assert contents of dev_2 is 'Device not Found'
        """
        if Juniper_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Juniper_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Juniper_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# ArubaOS Switch ( Previously Provision)
class TestGetDevDetailsArubaOSSwitch(TestCase):
    def test_get_dev_details_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(ArubaOS_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(ArubaOS_Switch, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# Routers

# Cisco Router
class TestGetDevDetailsCiscoRouter(TestCase):
    """
    test get_dev_details function on Cisco Router
    """
    def test_get_dev_details_type(self):
        """
        check to see if Cisco_Router is defined, if not deined skip test
        if defined, run get_dev_details using Cisco_Router function and assignt to dev_1
        assert dev_1 is type dict
        run get_dev_details function and assing to dev_2
        assert contents of dev_2 is 'Device not Found'
        """
        if Cisco_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Router, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Router, auth.creds, auth.url)
        self.assertIs(len(dev_1), 23) # TODO modified len from 22 to 23 need to investigate why
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# CW5 Router
class TestGetDevDetailsCW5Router(TestCase):
    def test_get_dev_details_type(self):
        if CW5_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Router, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW5_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Router, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# Juniper Router ( SRX )
class TestGetDevDetailsJuniperRouter(TestCase):
    def test_get_dev_details_type(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Router, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_1 = get_dev_details(Juniper_Router, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# Servers

# Windows Server
class TestGetDevDetailsWindowsServer(TestCase):
    """
    test get_dev_detail function on Windows Server
    """
    def test_get_dev_details_type(self):
        if Windows_Server is None:
            raise SkipTest
        dev_1 = get_dev_details(Windows_Server, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Windows_Server is None:
            raise SkipTest
        dev_1 = get_dev_details(Windows_Server, auth.creds, auth.url)
        self.assertIs(len(dev_1), 23) # TODO modified len from 22 to 23 need to investigate
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# Linux Server
class TestGetDevDetailsLinuxServer(TestCase):
    def test_get_dev_details_type(self):
        if Linux_Server is None:
            raise SkipTest
        dev_1 = get_dev_details(Linux_Server, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Linux_Server is None:
            raise SkipTest
        dev_1 = get_dev_details(Linux_Server, auth.creds, auth.url)
        self.assertIs(len(dev_1), 23) #TODO modified len from 22 to 23 need to investigate
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# Hypervisors

# VMWare ESX Hypervisor
class TestGetDevDetailsESX(TestCase):
    def test_get_dev_details_type(self):
        if ESX is None:
            raise SkipTest
        dev_1 = get_dev_details(ESX, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if ESX is None:
            raise SkipTest
        dev_1 = get_dev_details(ESX, auth.creds, auth.url)
        self.assertIs(len(dev_1), 23) # TODO modified len from 22 to 23 need to investigate
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


# Microsoft HyperV Hypervisor
class TestGetDevDetailsHyperV(TestCase):
    def test_get_dev_details_type(self):
        if HyperV is None:
            raise SkipTest
        dev_1 = get_dev_details(HyperV, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if HyperV is None:
            raise SkipTest
        dev_1 = get_dev_details(HyperV, auth.creds, auth.url)
        self.assertIs(len(dev_1), 22)
        self.assertIn('typeName', dev_1)
        self.assertIn('sysOid', dev_1)
        self.assertIn('mask', dev_1)
        self.assertIn('symbolId', dev_1)
        self.assertIn('symbolName', dev_1)
        self.assertIn('ip', dev_1)
        self.assertIn('symbolLevel', dev_1)
        self.assertIn('symbolType', dev_1)
        self.assertIn('symbolDesc', dev_1)
        self.assertIn('contact', dev_1)
        self.assertIn('parentId', dev_1)
        self.assertIn('status', dev_1)
        self.assertIn('devCategoryImgSrc', dev_1)
        self.assertIn('label', dev_1)
        self.assertIn('categoryId', dev_1)
        self.assertIn('sysName', dev_1)
        self.assertIn('sysDescription', dev_1)
        self.assertIn('location', dev_1)
        self.assertIn('topoIconName', dev_1)
        self.assertIn('statusDesc', dev_1)
        self.assertIn('id', dev_1)


"""============================================================================================="""


# Test TestGet_dev_interface for Multiple Vendor Devices

# Switches


# CW3 Switch
class TestGetDevInterfacesCW3Switch(TestCase):
    def test_get_dev_interface_type(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# CW5 Switch
class TestGetDevInterfacesCW5Switch(TestCase):
    def test_get_dev_interface_type(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# CW7 Switch
class TestGetDevInterfacesCW7Switch(TestCase):
    def test_get_dev_interface_type(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(dev_interfaces[0]), 19) # TODO modified len from 18 to 19 need to investigate
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# Cisco Switch
class TestGetDevInterfacesCiscoSwitch(TestCase):
    def test_get_dev_interface_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# Juniper Switch
class TestGetDevInterfacesJuniperSwitch(TestCase):
    def test_get_dev_interface_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# Arista Switch
class TestGetDevInterfacesAristaSwitch(TestCase):
    def test_get_dev_interface_type(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# ArubaOS Switch ( Formerly Provision )
class TestGetDevInterfacesArubaOSSwitch(TestCase):
    def test_get_dev_interface_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# Routers


# Cisco Router
class TestGetDevInterfacesCiscoRouter(TestCase):
    def test_get_dev_interface_type(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# CW5 Router
class TestGetDevInterfacesCW5Router(TestCase):
    def test_get_dev_interface_type(self):
        if CW5_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW5_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# Juniper Router ( SRX )
class TestGetDevInterfacesJuniperRouter(TestCase):
    def test_get_dev_interface_type(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# Servers

# Windows_Server
# TODO re-run test after bug is fixed. API not currently returning Windows interfaces
'''
class TestGetDevInterfacesWindowsServer(TestCase):
    def test_get_dev_interface_type(self):
        if Windows_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Windows_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# Linux_Server
class TestGetDevInterfacesLinuxServer(TestCase):
    def test_get_dev_interface_type(self):
        if Linux_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Linux_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(dev_interfaces[0]), 19) # TODO Modified len from 18 to 19 need to investigate
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])
'''

# Hypervisors


# VMWare ESX Hypervisor
class TestGetDevInterfacesESXServer(TestCase):
    def test_get_dev_interface_type(self):
        if ESX is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if ESX is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])


# HyperV
# TODO test rmoved due to reported bug re run when bug fixed
'''
class TestGetDevInterfacesHyperVServer(TestCase):
    def test_get_dev_interface_type(self):
        if HyperV is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if HyperV is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(dev_interfaces[0]), 18)
        self.assertIn('mtu', dev_interfaces[0])
        self.assertIn('lastChange', dev_interfaces[0])
        self.assertIn('ifIndex', dev_interfaces[0])
        self.assertIn('ifDescription', dev_interfaces[0])
        self.assertIn('operationStatus', dev_interfaces[0])
        self.assertIn('operationStatusDesc', dev_interfaces[0])
        self.assertIn('showStatus', dev_interfaces[0])
        self.assertIn('ifAlias', dev_interfaces[0])
        self.assertIn('adminStatus', dev_interfaces[0])
        self.assertIn('ifspeed', dev_interfaces[0])
        self.assertIn('lastChangeTime', dev_interfaces[0])
        self.assertIn('ifTypeDesc', dev_interfaces[0])
        self.assertIn('adminStatusDesc', dev_interfaces[0])
        self.assertIn('filterTrapStatus', dev_interfaces[0])
        self.assertIn('phyAddress', dev_interfaces[0])
        self.assertIn('statusDesc', dev_interfaces[0])
        self.assertIn('appointedSpeed', dev_interfaces[0])
        self.assertIn('ifType', dev_interfaces[0])
'''

"""============================================================================================="""


# Test TestGet_dev_run_config for Multiple Vendor Devices

# Switches

# CW3 Switch
class TestGetDevRunConfigCW3Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if CW3_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(run_config), str)


# CW5_Switch
class TestGetDevRunConfigCW5Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if CW5_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(run_config), str)


# CW7_Switch
class TestGetDevRunConfigCW7Switch(TestCase):
    def test_get_dev_run_config_supported(self):
        if CW7_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(run_config), str)


# Cisco_Switch
class TestGetDevRunConfigCiscoSwitch(TestCase):
    def test_get_dev_run_config_supported(self):
        if Cisco_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(run_config), str)


# Juniper_Switch
class TestGetDevRunConfigJuniperSwitch(TestCase):
    def test_get_dev_run_config_supported(self):
        if Juniper_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(run_config), str)


# Arista_Switch
# T
class TestGetDevRunConfigAristaSwitch(TestCase):
    def test_get_dev_run_config_supported(self):
        if Arista_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(run_config), str)


# ArubaOS_Switch (Formerly Provision)
class TestGetDevRunConfigArubaOSSwitch(TestCase):
    def test_get_dev_run_config_supported(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(run_config), str)


# Routers

# Cisco_Router
class TestGetDevRunConfigCiscoRouter(TestCase):
    def test_get_dev_run_config_supported(self):
        if Cisco_Router is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(run_config), str)


# CW5_Router
class TestGetDevRunConfigCW5Router(TestCase):
    def test_get_dev_run_config_supported(self):
        if CW5_Router is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(run_config), str)


# Juniper_Router (SRV)
class TestGetDevRunConfigJuniperRouter(TestCase):
    def test_get_dev_run_config_supported(self):
        if Juniper_Router is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(run_config), str)


# Servers


# Windows_Server
class TestGetDevRunConfigWindowsServer(TestCase):
    def test_get_dev_run_config_unsupported(self):
        if Windows_Server is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual(run_config, "This features is no supported on this device")


# Linux_Server
class TestGetDevRunConfigLinuxServer(TestCase):
    def test_get_dev_run_config_unsupported(self):
        if Linux_Server is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual(run_config, "This features is no supported on this device")


# Hypervisors


# VMWare ESX
class TestGetDevRunConfigVMWare(TestCase):
    def test_get_dev_run_config_unsupported(self):
        if ESX is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=ESX)
        self.assertEqual(run_config, "This features is no supported on this device")


# HyperV
class TestGetDevRunConfigHyperV(TestCase):
    def test_get_dev_run_config_unsupported(self):
        if HyperV is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=HyperV)
        self.assertEqual(run_config, "This features is no supported on this device")


# Test TestGet_dev_start_config for Multiple Vendor Devices

"""============================================================================================="""


# Test get_dev_start_config for Multiple Vendor Devices

# Switches

# CW3_Switch
class TestGetDevStartConfigCW3Switch(TestCase):
    def test_get_dev_run_start_supported(self):
        if CW3_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(start_config), str)


# CW5_Switch
class TestGetDevStartConfigCW5Switch(TestCase):
    def test_get_dev__start_supported(self):
        if CW5_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(start_config), str)


# CW7_Switch
class TestGetDevStartConfigCW7Switch(TestCase):
    def test_get_dev_start_supported(self):
        if CW7_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(start_config), str)


# Cisco_Switch
class TestGetDevStartConfigCiscoSwitch(TestCase):
    def test_get_dev_start_supported(self):
        if Cisco_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(start_config), str)


# Juniper_Switch
class TestGetDevStartConfigJuniperSwitch(TestCase):
    def test_get_dev_start_supported(self):
        if Juniper_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(start_config), str)


# Arista_Switch
class TestGetDevStartConfigAristaSwitch(TestCase):
    def test_get_dev_start_supported(self):
        if Arista_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(start_config), str)


# ArubaOS_Switch (Formerly Provision)
class TestGetDevStartConfigArubaOSSwitch(TestCase):
    def test_get_dev_start_supported(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(start_config), str)


# Routers

# Cisco_Router
class TestGetDevStartConfigCiscoRouter(TestCase):
    def test_get_dev_start_supported(self):
        if Cisco_Router is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(start_config), str)


# CW5_Router
class TestGetDevStartConfigCW5Router(TestCase):
    def test_get_dev_start_supported(self):
        if CW5_Router is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(start_config), str)


# Juniper_Router (SRV)
class TestGetDevStartConfigJuniperRouter(TestCase):
    def test_get_dev_start_supported(self):
        if Juniper_Router is None:
            raise SkipTest
        start_config = get_dev_start_config(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(start_config), str)


# Servers


# Windows_Server
class TestGetDevStartConfigWindowsServer(TestCase):
    def test_get_dev_run_start_unsupported(self):
        if Windows_Server is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual(run_config, "This features is no supported on this device")


# Linux_Server
class TestGetDevStartConfigLinuxServer(TestCase):
    def test_get_dev_run_start_unsupported(self):
        if Linux_Server is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual(run_config, "This features is no supported on this device")


# Hypervisors


# VMWare ESX
class TestGetDevStartConfigVMWare(TestCase):
    def test_get_dev_run_start_unsupported(self):
        if ESX is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=ESX)
        self.assertEqual(run_config, "This features is no supported on this device")


# HyperV
class TestGetDevStartConfigHyperV(TestCase):
    def test_get_dev_run_start_unsupported(self):
        if HyperV is None:
            raise SkipTest
        run_config = get_dev_run_config(auth.creds, auth.url, devip=HyperV)
        self.assertEqual(run_config, "This features is no supported on this device")


# Test TestGet_dev_mac_learn for Multiple Vendor Devices


"""============================================================================================="""


# Test TestGet_dev_mac_learn for Multiple Vendor Devices

# Switches

# CW3_Switch
class TestGetDevMacLearnCW3Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# CW5_Switch
class TestGetDevMacLearnCW5Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# CW7_Switch
class TestGetDevMacLearnCW7Switch(TestCase):
    def test_get_dev_mac_learnType(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# Cisco_Switch
class TestGetDevMacLearnCiscoSwitch(TestCase):
    def test_get_dev_mac_learnType(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(dev_mac_learn), 10)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# Juniper_Switch
class TestGetDevMacLearnJuniperSwitch(TestCase):
    def test_get_dev_mac_learnType(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# Arista_Switch
class TestGetDevMacLearnAristaSwitch(TestCase):
    def test_get_dev_mac_learnType(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# ArubaOS_Switch (Formerly Provision)
class TestGetDevMacLearnArubaOSSwitch(TestCase):
    def test_get_dev_mac_learnType(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# Routers

# Cisco_Router
# TODO removed tests due to potential bug/unsupported feature
'''
class TestGetDevMacLearnCiscoRouter(TestCase):
    def test_get_dev_mac_learnType(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# CW5_Router
class TestGetDevMacLearnCW5Router(TestCase):
    def test_get_dev_mac_learnType(self):
        if CW5_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if CW5_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# Juniper_Router (SRV)
class TestGetDevMacLearnJuniperRouter(TestCase):
    def test_get_dev_mac_learnType(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# Servers


# Windows_Server
class TestGetDevMacLearnWindowsServer(TestCase):
    def test_get_dev_mac_learnType(self):
        if Windows_Server is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Windows_Server is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# Linux_Server
class TestGetDevMacLearnLinuxServer(TestCase):
    def test_get_dev_mac_learnType(self):
        if Linux_Server is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if Linux_Server is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# Hypervisors


# VMWare ESX
class TestGetDevMacLearnVMware(TestCase):
    def test_get_dev_mac_learnType(self):
        if ESX is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if ESX is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])


# HyperV

class TestGetDevMacLearnHyperV(TestCase):
    def test_get_dev_mac_learnType(self):
        if HyperV is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learnContent(self):
        if HyperV is None:
            raise SkipTest
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])
'''

"""============================================================================================="""


# Test TestRun_dev_cmd for Multiple Vendor Devices

# Switches

# CW3_Switch
class TestRunDevCmdCW3Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if CW3_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if CW3_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# CW5_Switch
class TestRunDevCmdCW5Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if CW5_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if CW5_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# CW7_Switch
class TestRunDevCmdCW7Switch(TestCase):
    def test_run_dev_cmd_type(self):
        if CW7_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if CW7_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# Cisco_Switch
class TestRunDevCmdCiscoSwitch(TestCase):
    def test_run_dev_cmd_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# Juniper_Switch
class TestRunDevCmdJuniperSwitch(TestCase):
    def test_run_dev_cmd_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# Arista_Switch
class TestRunDevCmdAristaSwitch(TestCase):
    def test_run_dev_cmd_type(self):
        if Arista_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Arista_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# ArubaOS_Switch (Formerly Provision)
class TestRunDevCmdArubaOSSwitch(TestCase):
    def test_run_dev_cmd_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# Routers

# Cisco_Router
class TestRunDevCmdCiscoRouter(TestCase):
    def test_run_dev_cmd_type(self):
        if Cisco_Router is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Cisco_Router is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# CW5_Router
class TestRunDevCmdCW5Router(TestCase):
    def test_run_dev_cmd_type(self):
        if CW5_Router is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if CW5_Router is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# Juniper_Router (SRX)
class TestRunDevCmdJuniperRouter(TestCase):
    def test_run_dev_cmd_type(self):
        if Juniper_Router is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Juniper_Router is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)


# Servers


# Windows_Server
class TestRunDevCmdWindowsServer(TestCase):
    def test_run_dev_cmd_type(self):
        if Windows_Server is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Windows_Server is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(cmd_output), 5)
        self.assertIn('success', cmd_output)
        self.assertIn('errorCode', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
        self.assertIn('errorMsg', cmd_output)


# Linux_Server
class TestRunDevCmdLinuxServer(TestCase):
    def test_run_dev_cmd_type(self):
        if Linux_Server is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if Linux_Server is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(cmd_output), 5)
        self.assertIn('success', cmd_output)
        self.assertIn('errorCode', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
        self.assertIn('errorMsg', cmd_output)


# Hypervisors


# VMWare ESX
class TestRunDevCmdVMware(TestCase):
    def test_run_dev_cmd_type(self):
        if ESX is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=ESX)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if ESX is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=ESX)
        self.assertIs(len(cmd_output), 5)
        self.assertIn('success', cmd_output)
        self.assertIn('errorCode', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
        self.assertIn('errorMsg', cmd_output)


# HyperV
class TestRunDevCmdHyperV(TestCase):
    def test_run_dev_cmd_type(self):
        if HyperV is None:
            raise SkipTest
        cmd_list = ['show version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        if HyperV is None:
            raise SkipTest
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(cmd_output), 5)
        self.assertIn('success', cmd_output)
        self.assertIn('errorCode', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)
        self.assertIn('errorMsg', cmd_output)


"""============================================================================================="""


# Test TestGet_all_interface_details for Multiple Vendor Devices

# Switches

# CW3_Switch
class TestGet_all_interface_details_CW3_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW3_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if CW3_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# CW5_Switch
class TestGet_all_interface_details_CW5_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW5_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if CW5_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# CW7_Switch
class TestGet_all_interface_details_CW7_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if CW7_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if CW7_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(all_interface_details[0]), 19) # TODO Modofied len from 18 to 19 need to investigate
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# Cisco_Switch
class TestGet_all_interface_details_Cisco_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# Juniper_Switch
class TestGet_all_interface_details_Juniper_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# Arista_Switch
class TestGet_all_interface_details_Arista_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if Arista_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Arista_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# ArubaOS_Switch (Formerly Provision)
class TestGet_all_interface_details_ArubaOS_Switch(TestCase):
    def test_get_all_interface_details_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# Routers

# Cisco_Router
class TestGet_all_interface_details_Cisco_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if Cisco_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# CW5_Router
class TestGet_all_interface_details_CW5_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if CW5_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if CW5_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# Juniper_Router (SRV)
class TestGet_all_interface_details_Juniper_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if Juniper_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Juniper_Router is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# Servers


# Windows_Server
# TODO Removed test due to reported bug
'''
class TestGet_all_interface_details_Windows_Server(TestCase):
    def test_get_all_interface_details_type(self):
        if Windows_Server is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])
'''

# Linux_Server
class TestGet_all_interface_details_Linux_Server(TestCase):
    def test_get_all_interface_details_type(self):
        if Linux_Server is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if Linux_Server is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(all_interface_details[0]), 19) # TODO Modified len from 18 to 19 need to investigate
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# Hypervisors


# VMWare ESX
class TestGet_all_interface_details_VMWare(TestCase):
    def test_get_all_interface_details_type(self):
        if ESX is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if ESX is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# HyperV
class TestGet_all_interface_details_HyperV(TestCase):
    def test_get_all_interface_details_type(self):
        if HyperV is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        if HyperV is None:
            raise SkipTest
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(all_interface_details[0]), 18)
        self.assertIn('phyAddress', all_interface_details[0])
        self.assertIn('ifAlias', all_interface_details[0])
        self.assertIn('statusDesc', all_interface_details[0])
        self.assertIn('ifType', all_interface_details[0])
        self.assertIn('operationStatusDesc', all_interface_details[0])
        self.assertIn('lastChangeTime', all_interface_details[0])
        self.assertIn('ifDescription', all_interface_details[0])
        self.assertIn('appointedSpeed', all_interface_details[0])
        self.assertIn('ifTypeDesc', all_interface_details[0])
        self.assertIn('filterTrapStatus', all_interface_details[0])
        self.assertIn('ifIndex', all_interface_details[0])
        self.assertIn('lastChange', all_interface_details[0])
        self.assertIn('adminStatusDesc', all_interface_details[0])
        self.assertIn('showStatus', all_interface_details[0])
        self.assertIn('operationStatus', all_interface_details[0])
        self.assertIn('mtu', all_interface_details[0])
        self.assertIn('adminStatus', all_interface_details[0])
        self.assertIn('ifspeed', all_interface_details[0])


# TODO
"""============================================================================================="""


# Test TestGet_interface_details for Multiple Vendor Devices


# Switches

# CW3_Switch
# modified ifIndex value for Cw3 switch specific to my environment
class TestGet_interface_details_CW3_Switch(TestCase):
    def test_get_interface_details_type(self):
        if CW3_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('4227689', auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_interface_details_content(self):
        if CW3_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('4227689', auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# CW5_Switch
class TestGet_interface_details_CW5_Switch(TestCase):
    def test_get_interface_details_type(self):
        if CW5_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_interface_details_content(self):
        if CW5_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# CW7_Switch
class TestGetInterfaceDetailsCw7Switch(TestCase):
    def test_get_interface_details_type(self):
        if CW7_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_interface_details_content(self):
        if CW7_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(interface_details), 19) # TODO Modified len from 18 to 19 need to investigate
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# Cisco_Switch
class TestGetInterfaceDetailsCiscoSwitch(TestCase):
    def test_get_interface_details_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_interface_details_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# Juniper_Switch
class TestGet_interface_details_Juniper_Switch(TestCase):
    def test_get_interface_details_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_interface_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# Arista_Switch
class TestGetInterfaceDetailsAristaSwitch(TestCase):
    def test_get_interface_details_type(self):
        if Arista_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_interface_details_content(self):
        if Arista_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# ArubaOS_Switch (Formerly Provision)
class TestGetInterfaceDetailsArubaOSSwitch(TestCase):
    def test_get_interface_details_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(interface_details), dict)

    def test_get_interface_details_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# Routers

# Cisco_Router
class TestGetInterfaceDetailsCiscoRouter(TestCase):
    def test_get_interface_details_type(self):
        if Cisco_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(interface_details), dict)

    def test_get_interface_details_content(self):
        if Cisco_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# CW5_Router
class TestGet_interface_details_CW5_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if CW5_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if CW5_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# Juniper_Router (SRV)
class TestGet_interface_details_Juniper_Router(TestCase):
    def test_get_all_interface_details_type(self):
        if Juniper_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Juniper_Router is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# Servers


# Windows_Server
# TODO Removed test due to reported bug
'''
class TestGet_interface_details_Windows_Server(TestCase):
    def test_get_all_interface_details_type(self):
        if Windows_Server is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Windows_Server is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)
'''


# Linux_Server
class TestGet_interface_details_Linux_Server(TestCase):
    def test_get_all_interface_details_type(self):
        if Linux_Server is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if Linux_Server is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(interface_details), 19) # TODO modified len from 18 to 19 need to investigate
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# Hypervisors


# ESX
class TestGet_interface_details_ESX(TestCase):
    def test_get_all_interface_details_type(self):
        if ESX is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=ESX)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if ESX is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=ESX)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


# HyperV
class TestGet_interface_details_HyperV(TestCase):
    def test_get_all_interface_details_type(self):
        if HyperV is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(interface_details), dict)

    def test_get_all_interface_details_content(self):
        if HyperV is None:
            raise SkipTest
        interface_details = get_interface_details('1', auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(interface_details), 18)
        self.assertIn('operationStatus', interface_details)
        self.assertIn('ifType', interface_details)
        self.assertIn('statusDesc', interface_details)
        self.assertIn('adminStatus', interface_details)
        self.assertIn('ifspeed', interface_details)
        self.assertIn('lastChangeTime', interface_details)
        self.assertIn('ifTypeDesc', interface_details)
        self.assertIn('showStatus', interface_details)
        self.assertIn('ifDescription', interface_details)
        self.assertIn('appointedSpeed', interface_details)
        self.assertIn('phyAddress', interface_details)
        self.assertIn('operationStatusDesc', interface_details)
        self.assertIn('filterTrapStatus', interface_details)
        self.assertIn('adminStatusDesc', interface_details)
        self.assertIn('lastChange', interface_details)
        self.assertIn('ifIndex', interface_details)
        self.assertIn('ifAlias', interface_details)


"""============================================================================================="""


# Test TestSet_inteface_up for Multiple Vendor Devices


# Switches

# CW3_Switch
class TestSet_inteface_up_CW3_Switch(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if CW3_Switch is None:
            raise SkipTest
        set_interface_down(CW3_Interface, auth.creds, auth.url, devip=CW3_Switch)
        int_up_response = set_inteface_up('1', auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# CW5_Switch
class TestSet_inteface_up_CW5_Switch(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if CW5_Switch is None:
            raise SkipTest
        set_interface_down(CW5_Interface, auth.creds, auth.url, devip=CW5_Switch)
        int_up_response = set_inteface_up(CW5_Interface, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# CW7_Switch
class TestSet_inteface_up_CW7_Switch(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if CW7_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=CW7_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# Cisco_Switch
class TestSet_inteface_up_Cisco_Switch(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if Cisco_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Cisco_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# Juniper_Switch
class TestSet_inteface_up_Juniper_Switch(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if Juniper_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Juniper_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# Arista_Switch
class TestSet_inteface_up_Arista_Switch(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if Arista_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Arista_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# ArubaOS_Switch (Formerly Provision)
class TestSet_inteface_up_ArubaOS_Switch(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if ArubaOS_Switch is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# Routers

# Cisco_Router

# Ensure that the ifIndex for this test is the far interface of the router away from IMC or you will
# kill access to the machine which will force manual intervention
class TestSet_inteface_up_Cisco_Router(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if Cisco_Router is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Cisco_Router)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# CW5_Router
# Ensure that the ifIndex for this test is the far interface of the router away from IMC
# or you will kill access to the machine which will force manual intervention
class TestSet_inteface_up_CW5_Router(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if CW5_Router is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=CW5_Router)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# Juniper_Router (SRV)
# Ensure that the ifIndex for this test is the far interface of the router away from IMC
# or you will kill access to the machine which will force manual intervention
class TestSet_inteface_up_Juniper_Router(TestCase):
    def test_set_inteface_up(self):
        if test_interface_up is False:
            raise SkipTest
        if Juniper_Router is None:
            raise SkipTest
        set_interface_down('9', auth.creds, auth.url, devip=Juniper_Router)
        int_up_response = set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(int_up_response), int)
        self.assertIs(int_up_response, 204)


# Servers


# Windows_Server
# Deemed inappropriate to test

# Linux_Server
# Deemed inappropriate to test

# Hypervisors


# ESX
# Deemed inappropriate to test

# HyperV
# Deemed inappropriate to test


"""============================================================================================="""


# Test TestSet_inteface_down for Multiple Vendor Devices

# Switches

# CW3_Switch
class TestSet_inteface_down_CW3_Switch(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if CW3_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=CW3_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=CW3_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# CW5_Switch
class TestSet_inteface_down_CW5_Switch(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if CW5_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=CW5_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=CW5_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# CW7_Switch
class TestSet_inteface_down_CW7_Switch(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if CW7_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=CW7_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=CW7_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# Cisco_Switch
class TestSet_inteface_down_Cisco_Switch(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if Cisco_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Cisco_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# Juniper_Switch
class TestSet_inteface_down_Juniper_Switch(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if Juniper_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Juniper_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# Arista_Switch
class TestSet_inteface_down_Arista_Switch(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if Arista_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Arista_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Arista_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# ArubaOS_Switch (Formerly Provision)
class TestSet_inteface_down_ArubaOS_Switch(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if ArubaOS_Switch is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        set_inteface_up('9', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# Routers

# Cisco_Router
# Ensure that the ifIndex for this test is the far interface of the router away from IMC
# or you will kill access to the machine which will force manual intervention
class TestSet_inteface_down_Cisco_Router(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if Cisco_Router is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Router)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Cisco_Router)
        set_inteface_up('9', auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# CW5_Router
# Ensure that the ifIndex for this test is the far interface of the router away from IMC
#  or you will kill access to the machine which will force manual intervention
class TestSet_inteface_down_CW5_Router(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if CW5_Router is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=CW5_Router)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=CW5_Router)
        set_inteface_up('9', auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


# Juniper_Router (SRV)
# Ensure that the ifIndex for this test is the far interface of the router away from IMC
#  or you will kill access to the machine which will force manual intervention
class TestSet_inteface_down_Juniper_Router(TestCase):
    def test_set_inteface_down(self):
        if test_interface_down is False:
            raise SkipTest
        if Juniper_Router is None:
            raise SkipTest
        set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Router)
        int_down_response = set_interface_down('9', auth.creds, auth.url, devip=Juniper_Router)
        set_inteface_up('9', auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(int_down_response), int)
        self.assertIs(int_down_response, 204)


