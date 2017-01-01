# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.vlanm module.

"""

from unittest import TestCase

from nose.plugins.skip import SkipTest

from pyhpeimc.plat.vlanm import *
from test_machine import *


# Section for Get_dev_vlans function for multi-vendor testing

# CW5_Switch
class Test_Get_dev_vlans_CW5_Switch(TestCase):
    def test_get_dev_vlans_type(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(dev_vlans), list)

    def test_get_dev_vlans_content(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(dev_vlans[0]), 3)
        self.assertIn('vlanStatus', dev_vlans[0])
        self.assertIn('vlanName', dev_vlans[0])
        self.assertIn('vlanId', dev_vlans[0])


# CW7_Switch
class Test_Get_dev_vlans_CW7_Switch(TestCase):
    def test_get_dev_vlans_type(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_vlans), list)


    def test_get_dev_vlans_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(dev_vlans[0]), 3)
        self.assertIn('vlanStatus', dev_vlans[0])
        self.assertIn('vlanName', dev_vlans[0])
        self.assertIn('vlanId', dev_vlans[0])


# Cisco_Switch
class Test_Get_dev_vlans_Cisco_Switch(TestCase):
    def test_get_dev_vlans_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(dev_vlans), list)


    def test_get_dev_vlans_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(dev_vlans[0]), 3)
        self.assertIn('vlanStatus', dev_vlans[0])
        self.assertIn('vlanName', dev_vlans[0])
        self.assertIn('vlanId', dev_vlans[0])


# Juniper_Switch
class Test_Get_dev_vlans_Juniper_Switch(TestCase):
    def test_get_dev_vlans_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(dev_vlans), dict)

    def test_get_dev_vlans_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(dev_vlans), 1)
        self.assertIn('vlan', dev_vlans)


# Arista_Switch
class Test_Get_dev_vlans_Arista_Switch(TestCase):
    def test_get_dev_vlans_type(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(dev_vlans), list)

    def test_get_dev_vlans_content(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(dev_vlans[0]), 3)
        self.assertIn('vlanStatus', dev_vlans[0])
        self.assertIn('vlanName', dev_vlans[0])
        self.assertIn('vlanId', dev_vlans[0])


# ArubaOS_Switch (Formerly Provision)
class Test_Get_dev_vlans_ArubaOS_Switch(TestCase):
    def test_get_dev_vlans_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(dev_vlans), list)

    def test_get_dev_vlans_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(dev_vlans[0]), 3)
        self.assertIn('vlanStatus', dev_vlans[0])
        self.assertIn('vlanName', dev_vlans[0])
        self.assertIn('vlanId', dev_vlans[0])


# Routers

# Cisco_Router
class Test_Get_dev_vlans_Cisco_Router(TestCase):
    def test_get_dev_vlans_type(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(dev_vlans), dict)

    def test_get_dev_vlans_content(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(dev_vlans), 1)
        self.assertIn('vlan', dev_vlans)


# CW5_Router
class Test_Get_dev_vlans_CW5_Router(TestCase):
    def test_get_dev_vlans_type(self):
        if CW5_Router is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(dev_vlans), list)

    def test_get_dev_vlans_content(self):
        if CW5_Router is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(dev_vlans[0]), 3)
        self.assertIn('vlanStatus', dev_vlans[0])
        self.assertIn('vlanName', dev_vlans[0])
        self.assertIn('vlanId', dev_vlans[0])


# Juniper_Router (SRX)
class Test_Get_dev_vlans_Juniper_Router(TestCase):
    def test_get_dev_vlans_type(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(dev_vlans), dict)

    def test_get_dev_vlans_content(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(dev_vlans), 1)
        self.assertIn('vlan', dev_vlans)


# Servers


# Windows_Server
class Test_Get_dev_vlans_Windows_Server(TestCase):
    def test_get_dev_vlans_type(self):
        if Windows_Server is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(dev_vlans), dict)

    def test_get_dev_vlans_content(self):
        if Windows_Server is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(dev_vlans), 1)
        self.assertIn('vlan', dev_vlans)


# Linux_Server
class Test_Get_dev_vlans_Linux_Server(TestCase):
    def test_get_dev_vlans_type(self):
        if Linux_Server is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(dev_vlans), dict)

    def test_get_dev_vlans_content(self):
        if Linux_Server is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(dev_vlans), 1)
        self.assertIn('vlan', dev_vlans)


# Hypervisors


# ESX
class Test_Get_dev_vlans_ESX(TestCase):
    def test_get_dev_vlans_type(self):
        if ESX is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(dev_vlans), dict)

    def test_get_dev_vlans_content(self):
        if ESX is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(dev_vlans), 1)
        self.assertIn('vlan', dev_vlans)


# HyperV
class Test_Get_dev_vlans_HyperV(TestCase):
    def test_get_dev_vlans_type(self):
        if HyperV is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(dev_vlans), dict)

    def test_get_dev_vlans_content(self):
        if HyperV is None:
            raise SkipTest
        dev_vlans = get_dev_vlans(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(dev_vlans), 1)
        self.assertIn('vlan', dev_vlans)


# Section for get_trunk_interfaces function for multi-vendor testing

# CW3_Switch
class Test_Get_trunk_interfaces_CW3_Switch(TestCase):
    def test_get_trunk_interfaces_type(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(dev_trunks[0]), 3)
        self.assertIn('ifIndex', dev_trunks[0])
        self.assertIn('pvid', dev_trunks[0])
        self.assertIn('allowedVlans', dev_trunks[0])


# CW5_Switch
class Test_Get_trunk_interfaces_CW5_Switch(TestCase):
    def test_get_trunk_interfaces_type(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(dev_trunks[0]), 3)
        self.assertIn('ifIndex', dev_trunks[0])
        self.assertIn('pvid', dev_trunks[0])
        self.assertIn('allowedVlans', dev_trunks[0])


# CW7_Switch
class Test_Get_trunk_interfaces_CW7_Switch(TestCase):
    def test_get_trunk_interfaces_type(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(dev_trunks[0]), 3)
        self.assertIn('ifIndex', dev_trunks[0])
        self.assertIn('pvid', dev_trunks[0])
        self.assertIn('allowedVlans', dev_trunks[0])


# Cisco_Switch
class Test_Get_trunk_interfaces_Cisco_Switch(TestCase):
    def test_get_trunk_interfaces_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(dev_trunks[0]), 3)
        self.assertIn('ifIndex', dev_trunks[0])
        self.assertIn('pvid', dev_trunks[0])
        self.assertIn('allowedVlans', dev_trunks[0])


# Juniper_Switch
class Test_Get_trunk_interfaces_Juniper_Switch(TestCase):
    def test_get_trunk_interfaces_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(len(dev_trunks), 1)
        self.assertEqual(dev_trunks[0], 'No trunk inteface')


# Arista_Switch
class Test_Get_trunk_interfaces_Arista_Switch(TestCase):
    def test_get_trunk_interfaces_type(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(dev_trunks), list)

    def v(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(dev_trunks[0]), 3)
        self.assertIn('ifIndex', dev_trunks[0])
        self.assertIn('pvid', dev_trunks[0])
        self.assertIn('allowedVlans', dev_trunks[0])


# ArubaOS_Switch (Formerly Provision)
class Test_Get_trunk_interfaces_ArubaOS_Switch(TestCase):
    def test_get_dev_vlans_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(dev_trunks), list)

    def test_get_dev_vlans_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(dev_trunks[0]), 3)
        self.assertIn('ifIndex', dev_trunks[0])
        self.assertIn('pvid', dev_trunks[0])
        self.assertIn('allowedVlans', dev_trunks[0])


# Routers

# Cisco_Router
class Test_Get_trunk_interfaces_Cisco_Router(TestCase):
    def test_get_trunk_interfaces_type(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(len(dev_trunks), 1)
        self.assertEqual(dev_trunks[0], 'No trunk inteface')


# CW5_Router
class Test_Get_trunk_interfaces_CW5_Router(TestCase):
    def test_get_trunk_interfaces_type(self):
        if CW5_Router is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if CW5_Router is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(len(dev_trunks), 1)
        self.assertEqual(dev_trunks[0], 'No trunk inteface')


# Juniper_Router (SRX)
class Test_Get_trunk_interfaces_Juniper_Router(TestCase):
    def test_get_trunk_interfaces_type(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(len(dev_trunks), 1)
        self.assertEqual(dev_trunks[0], 'No trunk inteface')


# Servers


# Windows_Server
class Test_Get_trunk_interfaces_Windows_Server(TestCase):
    def test_get_trunk_interfaces_type(self):
        if Windows_Server is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if Windows_Server is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(len(dev_trunks), 1)
        self.assertEqual(dev_trunks[0], 'No trunk inteface')


# Linux_Server
class Test_Get_trunk_interfaces_Linux_Server(TestCase):
    def test_get_trunk_interfaces_type(self):
        if Linux_Server is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if Linux_Server is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(len(dev_trunks), 1)
        self.assertEqual(dev_trunks[0], 'No trunk inteface')


# Hypervisors


# ESX
class Test_Get_trunk_interfaces_ESX(TestCase):
    def test_get_trunk_interfaces_type(self):
        if ESX is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if ESX is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=ESX)
        self.assertIs(len(dev_trunks), 1)
        self.assertEqual(dev_trunks[0], 'No trunk inteface')


# HyperV
class Test_Get_trunk_interfaces_HyperV(TestCase):
    def test_get_trunk_interfaces_type(self):
        if HyperV is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(dev_trunks), list)

    def test_get_trunk_interfaces_content(self):
        if HyperV is None:
            raise SkipTest
        dev_trunks = get_trunk_interfaces(auth.creds, auth.url, devip=HyperV)
        self.assertIs(len(dev_trunks), 1)
        self.assertEqual(dev_trunks[0], 'No trunk inteface')


# Section for get_device_access_interfaces function for multi-vendor testing

# CW3_Switch
class Test_Get_device_access_interfaces_CW3_Switch(TestCase):
    def test_get_device_access_interfaces_type(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(dev_access[0]), 2)
        self.assertIn('ifIndex', dev_access[0])
        self.assertIn('pvid', dev_access[0])


# CW5_Switch
class Test_Get_device_access_interfaces_CW5_Switch(TestCase):
    def test_get_device_access_interfaces_type(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if CW5_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(dev_access[0]), 2)
        self.assertIn('ifIndex', dev_access[0])
        self.assertIn('pvid', dev_access[0])


# CW7_Switch
class Test_Get_device_access_interfaces_CW7_Switch(TestCase):
    def test_get_device_access_interfaces_type(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if CW7_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(dev_access[0]), 2)
        self.assertIn('ifIndex', dev_access[0])
        self.assertIn('pvid', dev_access[0])


# Cisco_Switch
class Test_Get_device_access_interfaces_Cisco_Switch(TestCase):
    def test_get_device_access_interfaces_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(len(dev_access[0]), 2)
        self.assertIn('ifIndex', dev_access[0])
        self.assertIn('pvid', dev_access[0])


# Juniper_Switch
class Test_Get_device_access_interfaces_Juniper_Switch(TestCase):
    def test_get_device_access_interfaces_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Juniper_Switch)
        self.assertEqual((dev_access[0]), 'No access inteface')


# Arista_Switch
class Test_Get_device_access_interfaces_Arista_Switch(TestCase):
    def test_get_device_access_interfaces_type(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if Arista_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(len(dev_access[0]), 2)
        self.assertIn('ifIndex', dev_access[0])
        self.assertIn('pvid', dev_access[0])


# ArubaOS_Switch (Formerly Provision)
class Test_Get_device_access_interfaces_ArubaOS_Switch(TestCase):
    def test_get_device_access_interfaces_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(len(dev_access[0]), 2)
        self.assertIn('ifIndex', dev_access[0])
        self.assertIn('pvid', dev_access[0])


# Routers

# Cisco_Router
class Test_Get_device_access_interfaces_Cisco_Router(TestCase):
    def test_get_device_access_interfaces_type(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Cisco_Router)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if Cisco_Router is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Cisco_Router)
        self.assertEqual((dev_access[0]), 'No access inteface')


# CW5_Router
class Test_Get_device_access_interfaces_CW5_Router(TestCase):
    def test_get_device_access_interfaces_type(self):
        if CW5_Router is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=CW5_Router)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if CW5_Router is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=CW5_Router)
        self.assertEqual((dev_access[0]), 'No access inteface')


# Juniper_Router (SRX)
class Test_Get_device_access_interfaces_Juniper_Router(TestCase):
    def test_get_device_access_interfaces_type(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Juniper_Router)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if Juniper_Router is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Juniper_Router)
        self.assertEqual((dev_access[0]), 'No access inteface')


# Servers


# Windows_Server
class Test_Get_device_access_interfaces_Windows_Server(TestCase):
    def test_get_device_access_interfaces_type(self):
        if Windows_Server is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Windows_Server)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if Windows_Server is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual((dev_access[0]), 'No access inteface')


# Linux_Server
class Test_Get_device_access_interfaces_Linux_Server(TestCase):
    def test_get_device_access_interfaces_type(self):
        if Linux_Server is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Linux_Server)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if Linux_Server is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual((dev_access[0]), 'No access inteface')


# Hypervisors


# ESX
class Test_Get_device_access_interfaces_ESX(TestCase):
    def test_get_device_access_interfaces_type(self):
        if ESX is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=ESX)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if ESX is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=ESX)
        self.assertEqual((dev_access[0]), 'No access inteface')


# HyperV
class Test_Get_device_access_interfaces_HyperV(TestCase):
    def test_get_device_access_interfaces_type(self):
        if HyperV is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=HyperV)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if HyperV is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=HyperV)
        self.assertEqual((dev_access[0]), 'No access inteface')


# Multi-Vendor tests for create_dev_vlan function

# CW3_Switch
class Test_Create_dev_vlan_CW3_Switch(TestCase):
    def test_create_dev_vlan(self):
        if CW3_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(set_vlan, 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW3_Switch)


# CW5_Switch
class Test_Create_dev_vlan_CW5_Switch(TestCase):
    def test_create_dev_vlan(self):
        if CW5_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(set_vlan, 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW5_Switch)


# CW7_Switch
class Test_Create_dev_vlan_CW7_Switch(TestCase):
    def test_create_dev_vlan(self):
        if CW7_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(set_vlan, 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW7_Switch)


# Cisco_Switch
class Test_Create_dev_vlan_Cisco_Switch(TestCase):
    def test_create_dev_vlan(self):
        if Cisco_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertEqual(set_vlan, 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Cisco_Switch)


# Juniper_Switch
class Test_Create_dev_vlan_Juniper_Switch(TestCase):
    def test_create_dev_vlan(self):
        if Juniper_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Juniper_Switch)
        self.assertEqual(set_vlan, 409)


# Arista_Switch
# TODO Remarked Test until Arista VLANM is supported
'''
class Test_Create_dev_vlan_Arista_Switch(TestCase):
    def test_create_dev_vlan(self):
        if Arista_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Arista_Switch)
        self.assertEqual(set_vlan, 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Arista_Switch)
'''


# ArubaOS_Switch (Formerly Provision)
class Test_Create_dev_vlan_ArubaOS_Switch(TestCase):
    def test_create_dev_vlan(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertEqual(set_vlan, 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=ArubaOS_Switch)


# Routers


# Cisco_Router
class Test_Create_dev_vlan_Cisco_Router(TestCase):
    def test_create_dev_vlan(self):
        if Cisco_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Cisco_Router)
        self.assertEqual(set_vlan, 409)


# CW5_Router
class Test_Create_dev_vlan_CW5_Router(TestCase):
    def test_create_dev_vlan(self):
        if CW5_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW5_Router)
        self.assertEqual(set_vlan, 409)


# Juniper_Router (SRX)
class Test_Create_dev_vlan_Juniper_Router(TestCase):
    def test_create_dev_vlan(self):
        if Juniper_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Juniper_Router)
        self.assertEqual(set_vlan, 409)


# Servers


# Windows_Server
class Test_Create_dev_vlan_Windows_Server(TestCase):
    def test_create_dev_vlan(self):
        if Windows_Server is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual(set_vlan, 409)


# Linux_Server
class Test_Create_dev_vlan_Linux_Server(TestCase):
    def test_create_dev_vlan(self):
        if Linux_Server is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual(set_vlan, 409)


# Hypervisors


# ESX
class Test_Create_dev_vlan_ESX(TestCase):
    def test_create_dev_vlan(self):
        if ESX is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ESX)
        self.assertEqual(set_vlan, 409)


# HyperV
class Test_Create_dev_vlan_HyperV(TestCase):
    def test_create_dev_vlan(self):
        if HyperV is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ESX)
        self.assertEqual(set_vlan, HyperV)


# Test Delete_dev_vlans for Multiple Vendor Devices

# Switches

# CW3_Switch
class Test_Delete_dev_vlans_CW3_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if CW3_Switch is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW3_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if CW3_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(del_vlan, 409)


# CW5_Switch
class Test_Delete_dev_vlans_CW5_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if CW5_Switch is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW5_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if CW5_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(del_vlan, 409)


# CW7_Switch
class Test_Delete_dev_vlans_CW7_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if CW7_Switch is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW7_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if CW7_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(del_vlan, 409)


# Cisco_Switch
class Test_Delete_dev_vlans_Cisco_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if Cisco_Switch is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Cisco_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if Cisco_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertEqual(del_vlan, 409)


# Juniper_Switch
class Test_Delete_dev_vlans_Juniper_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if Juniper_Switch is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Juniper_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Juniper_Switch)
        self.assertEqual(del_vlan, 409)


# Arista_Switch
# TODO Remarked test until Arista VLANM is supported
'''
class Test_Delete_dev_vlans_Arista_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if Arista_Switch is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Arista_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if Arista_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Arista_Switch)
        self.assertEqual(del_vlan, 409)
'''

# ArubaOS_Switch (Formerly Provision)
class Test_Delete_dev_vlans_ArubaOS_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ArubaOS_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertEqual(del_vlan, 409)


# Routers

# Cisco_Router
class Test_Delete_dev_vlans_Cisco_Router(TestCase):
    def test_delete_dev_vlans(self):
        if Cisco_Router is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Cisco_Router)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Cisco_Router)
        self.assertEqual(del_vlan, 409)


# CW5_Router
class Test_Delete_dev_vlans_CW5_Router(TestCase):
    def test_delete_dev_vlans(self):
        if CW5_Router is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW5_Router)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW5_Router)
        self.assertEqual(del_vlan, 409)


# Juniper_Router (SRX)
class Test_Delete_dev_vlans_Juniper_Router(TestCase):
    def test_delete_dev_vlans(self):
        if Juniper_Router is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Juniper_Router)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Juniper_Router)
        self.assertEqual(del_vlan, 409)


# Servers


# Windows_Server
class Test_Delete_dev_vlans_Windows_Server(TestCase):
    def test_delete_dev_vlans(self):
        if Windows_Server is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Windows_Server)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual(del_vlan, 409)


# Linux_Server
class Test_Delete_dev_vlans_Linux_Server(TestCase):
    def test_delete_dev_vlans(self):
        if Linux_Server is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Linux_Server)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual(del_vlan, 409)


# Hypervisors


# ESX
class Test_Delete_dev_vlans_ESX(TestCase):
    def test_delete_dev_vlans(self):
        if ESX is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ESX)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=ESX)
        self.assertEqual(del_vlan, 409)


# HyperV
class Test_Delete_dev_vlans_HyperV(TestCase):
    def test_delete_dev_vlans(self):
        if HyperV is None:
            raise SkipTest
        create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=HyperV)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=HyperV)
        self.assertEqual(del_vlan, 409)


# Section for get_device_hybrid_interfaces function for multi-vendor testing

# CW3_Switch
# TODO Remarked test until cW3 interface is chosen
'''
class Test_Get_device_hybrid_interfaces_CW3_Switch(TestCase):
    def test_get_device_hybrid_interfaces_type(self):
        if CW3_Switch is None:
            raise SkipTest
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW3_Switch)
        dev_hybrid = get_device_hybrid_interfaces(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(type(dev_hybrid), list)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)

    def test_get_device_hybrid_interfaces_content(self):
        if CW3_Switch is None:
            raise SkipTest
        dev_hybrid = get_device_hybrid_interfaces(auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(len(dev_hybrid[0]), 5)
        self.assertIn('untaggedVlans', dev_hybrid[0])
        self.assertIn('taggedVlans', dev_hybrid[0])
        self.assertIn('untagVlanFlag', dev_hybrid[0])
        self.assertIn('ifIndex', dev_hybrid[0])
        self.assertIn('pvid', dev_hybrid[0])
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
'''


# CW5_Switch
class Test_Get_device_hybrid_interfaces_CW5_Switch(TestCase):
    def test_get_device_hybrid_interfaces_type(self):
        if CW5_Switch is None:
            raise SkipTest
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW5_Switch)
        dev_hybrid = get_device_hybrid_interfaces(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(type(dev_hybrid), list)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)

    def test_get_device_hybrid_interfaces_content(self):
        if CW5_Switch is None:
            raise SkipTest
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW5_Switch)
        dev_hybrid = get_device_hybrid_interfaces(auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(len(dev_hybrid[0]), 5)
        self.assertIn('untaggedVlans', dev_hybrid[0])
        self.assertIn('taggedVlans', dev_hybrid[0])
        self.assertIn('untagVlanFlag', dev_hybrid[0])
        self.assertIn('ifIndex', dev_hybrid[0])
        self.assertIn('pvid', dev_hybrid[0])
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)


# CW7_Switch
class Test_Get_device_hybrid_interfaces_CW7_Switch(TestCase):
    def test_get_device_hybrid_interfaces_type(self):
        if CW7_Switch is None:
            raise SkipTest
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW7_Switch)
        dev_hybrid = get_device_hybrid_interfaces(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(type(dev_hybrid), list)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)

    def test_get_device_hybrid_interfaces_content(self):
        if CW7_Switch is None:
            raise SkipTest
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW7_Switch)
        dev_hybrid = get_device_hybrid_interfaces(auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(len(dev_hybrid[0]), 5)
        self.assertIn('untaggedVlans', dev_hybrid[0])
        self.assertIn('taggedVlans', dev_hybrid[0])
        self.assertIn('untagVlanFlag', dev_hybrid[0])
        self.assertIn('ifIndex', dev_hybrid[0])
        self.assertIn('pvid', dev_hybrid[0])
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)


# Testing add_hybrid_interface for Comware Switches

# CW3_Switch
# TODO Investigate which interace to use for CW3 switch remove test until then
'''
class Test_Add_hybrid_interface_CW3_Switch(TestCase):
    def test_add_hybrid_interface(self):
        if CW3_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
        add_hybrid = add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(add_hybrid, 201)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)

    def test_add_hybrid_interface_already_exists(self):
        if CW3_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW3_Switch)
        add_hybrid = add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(add_hybrid, 409)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
'''


# CW5_Switch
class Test_Add_hybrid_interface_CW5_Switch(TestCase):
    def test_add_hybrid_interface(self):
        if CW5_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)
        add_hybrid = add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(add_hybrid, 201)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)

    def test_add_hybrid_interface_already_exists(self):
        if CW5_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW5_Switch)
        add_hybrid = add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(add_hybrid, 409)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)


# CW7_Switch
class Test_Add_hybrid_interface_CW7_Switch(TestCase):
    def test_add_hybrid_interface(self):
        if CW7_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)
        add_hybrid = add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(add_hybrid, 201)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)

    def test_add_hybrid_interface_already_exists(self):
        if CW7_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW7_Switch)
        add_hybrid = add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(add_hybrid, 409)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)


# Testing modify_hybrid_interface for Comware Switches

# CW3_Switch
# TODO Remarked test until cw3 interface selected
'''
class Test_Modify_hybrid_interface_CW3_Switch(TestCase):
    def test_modify_hybrid_interface(self):
        if CW3_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW3_Switch)
        modify_hybrid = modify_hybrid_interface('9', '1', '10,15', '1', auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(modify_hybrid, 204)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
'''


# CW5_Switch
class Test_Modify_hybrid_interface_CW5_Switch(TestCase):
    def test_modify_hybrid_interface(self):
        if CW5_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW5_Switch)
        modify_hybrid = modify_hybrid_interface('9', '1', '10,15', '1', auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(modify_hybrid, 204)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)


# CW7_Switch
class Test_Modify_hybrid_interface_CW7_Switch(TestCase):
    def test_modify_hybrid_interface(self):
        if CW7_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW7_Switch)
        modify_hybrid = modify_hybrid_interface('9', '1', '10,16', '1', auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(modify_hybrid, 204)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)


# Testing delete_hybrid_interface for Comware Switches

# CW3_Switch
# TODO Remarked test until CW3 interface is chosen
'''
class Test_Delete_hybrid_interface_CW3_Switch(TestCase):
    def test_delete_hybrid_interface(self):
        if CW3_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW3_Switch)
        delete_hybrid = delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(delete_hybrid, 204)

    def test_delete_hybrid_interface_doesnt_exists(self):
        if CW3_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
        delete_hybrid = delete_hybrid_interface('9', auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(delete_hybrid, 409)
'''


# CW5_Switch
class Test_Delete_hybrid_interface_CW5_Switch(TestCase):
    def test_delete_hybrid_interface(self):
        if CW5_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW5_Switch)
        delete_hybrid = delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(delete_hybrid, 204)

    def test_delete_hybrid_interface_doesnt_exists(self):
        if CW5_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)
        delete_hybrid = delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(delete_hybrid, 409)
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW5_Switch)


# CW7_Switch
class Test_Delete_hybrid_interface_CW7_Switch(TestCase):
    def test_delete_hybrid_interface(self):
        if CW7_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)
        add_hybrid_interface('9', '1', '10', '1', auth.creds, auth.url, devip=CW7_Switch)
        delete_hybrid = delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(delete_hybrid, 204)

    def test_delete_hybrid_interface_doesnt_exists(self):
        if CW7_Switch is None:
            raise SkipTest
        delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)
        delete_hybrid = delete_hybrid_interface('9', auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(delete_hybrid, 409)


# Test set_access_interface_pvid for Multi-Vendor Devices

# CW3_Switch
# TODO REmarked out test until cw3 interface selected
'''
class Test_Set_access_interface_pvid_CW3_Switch(TestCase):
    def test_set_access_interface_pvid(self):
        if CW3_Switch is None:
            raise SkipTest
        change_pvid = set_access_interface_pvid('9', '10', auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(change_pvid, 204)
        set_access_interface_pvid('9', '1', auth.creds, auth.url, devip=CW3_Switch)
'''


# CW5_Switch
class Test_Set_access_interface_pvid_CW5_Switch(TestCase):
    def test_set_access_interface_pvid(self):
        if CW5_Switch is None:
            raise SkipTest
        change_pvid = set_access_interface_pvid('9', '10', auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(change_pvid, 204)
        set_access_interface_pvid('9', '1', auth.creds, auth.url, devip=CW5_Switch)


# CW7_Switch
class Test_Set_access_interface_pvid_CW7_Switch(TestCase):
    def test_set_access_interface_pvid(self):
        if CW7_Switch is None:
            raise SkipTest
        change_pvid = set_access_interface_pvid('9', '10', auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(change_pvid, 204)
        set_access_interface_pvid('9', '1', auth.creds, auth.url, devip=CW7_Switch)


# Cisco_Switch
class Test_Set_access_interface_pvid_Cisco_Switch(TestCase):
    def test_set_access_interface_pvid(self):
        if Cisco_Switch is None:
            raise SkipTest
        change_pvid = set_access_interface_pvid('9', '10', auth.creds, auth.url, devip=Cisco_Switch)
        self.assertEqual(change_pvid, 204)
        set_access_interface_pvid('9', '1', auth.creds, auth.url, devip=Cisco_Switch)


# Juniper_Switch
class Test_Set_access_interface_pvid_Juniper_Switch(TestCase):
    def test_set_access_interface_pvid(self):
        if Juniper_Switch is None:
            raise SkipTest
        change_pvid = set_access_interface_pvid('9', '10', auth.creds, auth.url, devip=Juniper_Switch)
        self.assertEqual(change_pvid, 204)
        set_access_interface_pvid('9', '1', auth.creds, auth.url, devip=Juniper_Switch)


# Arista_Switch
# TODO Remarked out test until VLANM supports Arista
'''
class Test_Set_access_interface_pvid_Arista_Switch(TestCase):
    def test_set_access_interface_pvid(self):
        if Arista_Switch is None:
            raise SkipTest
        change_pvid = set_access_interface_pvid('9', '10', auth.creds, auth.url, devip=Arista_Switch)
        self.assertEqual(change_pvid, 204)
        set_access_interface_pvid('9', '1', auth.creds, auth.url, devip=Arista_Switch)
'''


# ArubaOS_Switch (Formerly Provision)
class Test_Set_access_interface_pvid_ArubaOS_Switch(TestCase):
    def test_set_access_interface_pvid(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        change_pvid = set_access_interface_pvid('9', '10', auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertEqual(change_pvid, 204)
        set_access_interface_pvid('9', '1', auth.creds, auth.url, devip=ArubaOS_Switch)
