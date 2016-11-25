from unittest import TestCase
from nose.plugins.skip import Skip, SkipTest

from pyhpeimc.tests.test_machine import *

from pyhpeimc.plat.device import *


class TestGet_all_devs(TestCase):
    def test_get_all_devs_type(self):
        dev_list = get_all_devs(auth.creds, auth.url)
        self.assertIs(type(dev_list), list)


    def test_get_all_devs_network_address_filter_type(self):
        dev_list = get_all_devs(auth.creds, auth.url, network_address='10.11.')
        self.assertIs(type(dev_list), list)

    def test_get_all_devs_content(self):
        dev_list = get_all_devs(auth.creds, auth.url, network_address='10.11.')
        self.assertIs(len(dev_list[0]), 23)
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
        self.assertIn('mac', dev_list[0])

#Test Get_Dev_Details for Multiple Vendor Devices
#Switches
class TestGet_dev_details_CW3_Switch(TestCase):
    def test_get_dev_details_type(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW3_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW3_Switch, auth.creds, auth.url)
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

class TestGet_dev_details_CW5_Switch(TestCase):
    def test_get_dev_details_type(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW5_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
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

class TestGet_dev_details_CW7_Switch(TestCase):
    def test_get_dev_details_type(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW7_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(CW7_Switch, auth.creds, auth.url)
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

class TestGet_dev_details_Cisco_Switch(TestCase):
    def test_get_dev_details_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Cisco_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
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

class TestGet_dev_details_Arista_Switch(TestCase):
    def test_get_dev_details_type(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Arista_Switch, auth.creds, auth.url)
        self.assertIs(type(dev_1), dict)
        dev_2 = get_dev_details('8.8.8.8', auth.creds, auth.url)
        self.assertIs(type(dev_2), str)
        self.assertEqual(dev_2, 'Device not found')

    def test_get_dev_details_content(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_1 = get_dev_details(Arista_Switch, auth.creds, auth.url)
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

class TestGet_dev_details_Juniper_Switch(TestCase):
    def test_get_dev_details_type(self):
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

class TestGet_dev_details_ArubaOS_Switch(TestCase):
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

#Routers
class TestGet_dev_details_Cisco_Router(TestCase):
    def test_get_dev_details_type(self):
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

class TestGet_dev_details_CW5_Router(TestCase):
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

class TestGet_dev_details_Juniper_Router(TestCase):
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

#Servers

class TestGet_dev_details_Windows_Server(TestCase):
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

class TestGet_dev_details_Linux_Server(TestCase):
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


#Hypervisors
class TestGet_dev_details_ESX(TestCase):
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

#Test TestGet_dev_interface for Multiple Vendor Devices


class TestGet_dev_interface_CW3_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip = CW3_Switch)
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

class TestGet_dev_interface_CW5_Switch(TestCase):
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

class TestGet_dev_interface_CW7_Switch(TestCase):
    def test_get_dev_interface_type(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=CW7_Switch)
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

class TestGet_dev_interface_Cisco_Switch(TestCase):
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

class TestGet_dev_interface_Juniper_Switch(TestCase):
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

class TestGet_dev_interface_Arista_Switch(TestCase):
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

class TestGet_dev_interface_ArubaOS_Switch(TestCase):
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

class TestGet_dev_interface_Cisco_Router(TestCase):
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

class TestGet_dev_interface_CW5_Router(TestCase):
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

class TestGet_dev_interface_Juniper_Router(TestCase):
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
class TestGet_dev_interface_Windows_Server(TestCase):
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
class TestGet_dev_interface_Linux_Server(TestCase):
    def test_get_dev_interface_type(self):
        if Linux_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(dev_interfaces), list)

    def test_get_dev_interface_content(self):
        if Linux_Server is None:
            raise SkipTest
        dev_interfaces = get_dev_interface(auth.creds, auth.url, devip=Linux_Server)
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
# Hypervisors
class TestGet_dev_interface_ESX_Server(TestCase):
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
class TestGet_dev_interface_HyperV_Server(TestCase):
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


#Test TestGet_dev_run_config for Multiple Vendor Devices

class TestGet_dev_run_config(TestCase):
    def test_get_dev_run_config_supported(self):
        run_config = get_dev_run_config(auth.creds, auth.url, devip='10.101.0.221')
        self.assertIs(type(run_config), str)

    def test_get_dev_run_config_unsupported(self):
        run_config = get_dev_run_config(auth.creds, auth.url, devip='10.101.0.51')
        self.assertEqual(run_config,"This features is no supported on this device")

#Test TestGet_dev_start_config for Multiple Vendor Devices

class TestGet_dev_start_config(TestCase):
    def test_get_dev_start_config_supported(self):
        start_config = get_dev_start_config(auth.creds, auth.url, devip='10.101.0.221')
        self.assertIs(type(start_config), str)

    def test_get_dev_run_config_unsupported(self):
        start_config = get_dev_start_config(auth.creds, auth.url, devip='10.101.0.51')
        self.assertEqual(start_config,"This features is no supported on this device")

#Test TestGet_dev_mac_learn for Multiple Vendor Devices
class TestGet_dev_mac_learn(TestCase):
    def test_get_dev_mac_learn_type(self):
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip='10.101.0.221')
        self.assertIs(type(dev_mac_learn), list)

    def test_get_dev_mac_learn_content(self):
        dev_mac_learn = get_dev_mac_learn(auth.creds, auth.url, devip='10.101.0.221')
        self.assertIs(len(dev_mac_learn[0]), 9)
        self.assertIn('deviceIp', dev_mac_learn[0])
        self.assertIn('learnIp', dev_mac_learn[0])
        self.assertIn('ifDesc', dev_mac_learn[0])
        self.assertIn('vlanId', dev_mac_learn[0])
        self.assertIn('learnMac', dev_mac_learn[0])
        self.assertIn('ifIndex', dev_mac_learn[0])
        self.assertIn('deviceId', dev_mac_learn[0])
        self.assertIn('iface', dev_mac_learn[0])
        self.assertIn('device', dev_mac_learn[0])

#Test TestRun_dev_cmd for Multiple Vendor Devices
class TestRun_dev_cmd_CW5_Switch(TestCase):
    def test_run_dev_cmd_type(self):
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(cmd_output), dict)

    def test_run_dev_cmd_content(self):
        cmd_list = ['display version']
        cmd_output = run_dev_cmd(cmd_list, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(cmd_output), 4)
        self.assertIn('success', cmd_output)
        self.assertIn('content', cmd_output)
        self.assertIn('cmdlist', cmd_output)
        self.assertIn('deviceId', cmd_output)

#Test TestGet_all_interface_details for Multiple Vendor Devices
class TestGet_all_interface_details(TestCase):
    def test_get_all_interface_details_type(self):
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip='10.101.0.221')
        self.assertIs(type(all_interface_details), list)

    def test_get_all_interface_details_content(self):
        all_interface_details = get_all_interface_details(auth.creds, auth.url, devip='10.101.0.221')
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




