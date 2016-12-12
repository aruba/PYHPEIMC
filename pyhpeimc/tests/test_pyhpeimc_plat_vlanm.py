from unittest import TestCase
from nose.plugins.skip import Skip, SkipTest
from pyhpeimc.tests.test_machine import *
from pyhpeimc.plat.vlanm import *


#Section for Get_dev_vlans function for multi-vendor testing

#CW5_Switch
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

#CW7_Switch
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


#Cisco_Switch
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


#Juniper_Switch
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


#Arista_Switch
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


#ArubaOS_Switch (Formerly Provision)
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


###Routers

#Cisco_Router
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


#CW5_Router
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


#Juniper_Router (SRX)
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


####Servers


#Windows_Server
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


#Linux_Server
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


###Hypervisors


#ESX
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


#HyperV
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


#Section for get_trunk_interfaces function for multi-vendor testing

#CW3_Switch
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


#CW5_Switch
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

#CW7_Switch
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


#Cisco_Switch
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

#Juniper_Switch
class Test_Get_dev_vlans_Juniper_Switch(TestCase):
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


#Arista_Switch
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


#ArubaOS_Switch (Formerly Provision)
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


###Routers

#Cisco_Router
class Test_Get_dev_vlans_Cisco_Router(TestCase):
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


#CW5_Router
class Test_Get_dev_vlans_CW5_Router(TestCase):
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


#Juniper_Router (SRX)
class Test_Get_dev_vlans_Juniper_Router(TestCase):
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


####Servers


#Windows_Server
class Test_Get_dev_vlans_Windows_Server(TestCase):
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


#Linux_Server
class Test_Get_dev_vlans_Linux_Server(TestCase):
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


###Hypervisors


#ESX
class Test_Get_dev_vlans_ESX(TestCase):
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


#HyperV
class Test_Get_dev_vlans_HyperV(TestCase):
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

#Section for get_device_access_interfaces function for multi-vendor testing

#CW3_Switch
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


#CW5_Switch
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



#CW7_Switch
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


#Cisco_Switch
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


#Juniper_Switch
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


#Arista_Switch
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


#ArubaOS_Switch (Formerly Provision)
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


###Routers

#Cisco_Router
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


#CW5_Router
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

#Juniper_Router (SRX)
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



####Servers


#Windows_Server
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



#Linux_Server
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

###Hypervisors


#ESX
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


#HyperV
class Test_Get_device_access_interfaces_HyperV(TestCase):
    def test_get_device_access_interfaces_type(self):
        if HyperV is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=HyperVv)
        self.assertIs(type(dev_access), list)

    def test_get_device_access_interfaces_content(self):
        if HyperV is None:
            raise SkipTest
        dev_access = get_device_access_interfaces(auth.creds, auth.url, devip=HyperV)
        self.assertEqual((dev_access[0]), 'No access inteface')


#Multi-Vendor tests for create_dev_vlan function

#CW3_Switch
class Test_Create_dev_vlan_CW3_Switch(TestCase):
    def test_create_dev_vlan(self):
        if CW3_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual((set_vlan), 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW3_Switch)


#CW5_Switch
class Test_Create_dev_vlan_CW5_Switch(TestCase):
    def test_create_dev_vlan(self):
        if CW5_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual((set_vlan), 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW5_Switch)


#CW7_Switch
class Test_Create_dev_vlan_CW7_Switch(TestCase):
    def test_create_dev_vlan(self):
        if CW7_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual((set_vlan), 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW7_Switch)


#Cisco_Switch
class Test_Create_dev_vlan_Cisco_Switch(TestCase):
    def test_create_dev_vlan(self):
        if Cisco_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertEqual((set_vlan), 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Cisco_Switch)


#Juniper_Switch
class Test_Create_dev_vlan_Juniper_Switch(TestCase):
    def test_create_dev_vlan(self):
        if Juniper_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Juniper_Switch)
        self.assertEqual((set_vlan), 409)

#Arista_Switch
class Test_Create_dev_vlan_Arista_Switch(TestCase):
    def test_create_dev_vlan(self):
        if Arista_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Arista_Switch)
        self.assertEqual((set_vlan), 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Arista_Switch)



#ArubaOS_Switch (Formerly Provision)
class Test_Create_dev_vlan_ArubaOS_Switch(TestCase):
    def test_create_dev_vlan(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertEqual((set_vlan), 201)
        delete_dev_vlans(vlanid, auth.creds, auth.url, devip=ArubaOS_Switch)


###Routers

#Cisco_Router
class Test_Create_dev_vlan_Cisco_Router(TestCase):
    def test_create_dev_vlan(self):
        if Cisco_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Cisco_Router)
        self.assertEqual((set_vlan), 409)

#CW5_Router
class Test_Create_dev_vlan_CW5_Router(TestCase):
    def test_create_dev_vlan(self):
        if CW5_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW5_Router)
        self.assertEqual((set_vlan), 409)

#Juniper_Router (SRX)
class Test_Create_dev_vlan_Juniper_Router(TestCase):
    def test_create_dev_vlan(self):
        if Juniper_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Juniper_Router)
        self.assertEqual((set_vlan), 409)


####Servers


#Windows_Server
class Test_Create_dev_vlan_Windows_Server(TestCase):
    def test_create_dev_vlan(self):
        if Windows_Server is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual((set_vlan), 409)



#Linux_Server
class Test_Create_dev_vlan_Linux_Server(TestCase):
    def test_create_dev_vlan(self):
        if Linux_Server is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual((set_vlan), 409)

###Hypervisors


#ESX
class Test_Create_dev_vlan_ESX(TestCase):
    def test_create_dev_vlan(self):
        if ESX is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ESX)
        self.assertEqual((set_vlan), 409)


#HyperV
class Test_Create_dev_vlan_HyperV(TestCase):
    def test_create_dev_vlan(self):
        if HyperV is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ESX)
        self.assertEqual((set_vlan), HyperV)


#####Test TEST_NAME_HERE for Multiple Vendor Devices

###Switches

#CW3_Switch
class Test_Delete_dev_vlans_CW3_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if CW3_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW3_Switch)
        del_vlan  = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW3_Switch)
        self.assertIs(del_vlan, 204)


    def test_delete_dev_vlans_doesnt_exist(self):
        if CW3_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW3_Switch)
        self.assertEqual(del_vlan, 409)


#CW5_Switch
class Test_Delete_dev_vlans_CW5_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if CW5_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW5_Switch)
        del_vlan  = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW5_Switch)
        self.assertIs(del_vlan, 204)


    def test_delete_dev_vlans_doesnt_exist(self):
        if CW5_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW5_Switch)
        self.assertEqual(del_vlan, 409)


#CW7_Switch
class Test_Delete_dev_vlans_CW7_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if CW7_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW7_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW7_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if CW7_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW7_Switch)
        self.assertEqual(del_vlan, 409)


#Cisco_Switch
class Test_Delete_dev_vlans_Cisco_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if Cisco_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Cisco_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if Cisco_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Cisco_Switch)
        self.assertEqual(del_vlan, 409)


#Juniper_Switch
class Test_Delete_dev_vlans_Juniper_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if Juniper_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Juniper_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Juniper_Switch)
        self.assertEqual(del_vlan, 409)


#Arista_Switch
class Test_Delete_dev_vlans_Arista_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if Arista_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Arista_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Arista_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if Arista_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Arista_Switch)
        self.assertEqual(del_vlan, 409)



#ArubaOS_Switch (Formerly Provision)
class Test_Delete_dev_vlans_ArubaOS_Switch(TestCase):
    def test_delete_dev_vlans(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ArubaOS_Switch)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertIs(del_vlan, 204)

    def test_delete_dev_vlans_doesnt_exist(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=ArubaOS_Switch)
        self.assertEqual(del_vlan, 409)


###Routers

#Cisco_Router
class Test_Delete_dev_vlans_Cisco_Router(TestCase):
    def test_delete_dev_vlans(self):
        if Cisco_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Cisco_Router)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Cisco_Router)
        self.assertEqual(del_vlan, 409)

#CW5_Router
class Test_Delete_dev_vlans_CW5_Router(TestCase):
    def test_delete_dev_vlans(self):
        if CW5_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=CW5_Router)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=CW5_Router)
        self.assertEqual(del_vlan, 409)

#Juniper_Router (SRX)
class Test_Delete_dev_vlans_Juniper_Router(TestCase):
    def test_delete_dev_vlans(self):
        if Juniper_Router is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Juniper_Router)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Juniper_Router)
        self.assertEqual(del_vlan, 409)


####Servers


#Windows_Server
class Test_Delete_dev_vlans_Windows_Server(TestCase):
    def test_delete_dev_vlans(self):
        if Windows_Server is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Windows_Server)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Windows_Server)
        self.assertEqual(del_vlan, 409)


#Linux_Server
class Test_Delete_dev_vlans_Linux_Server(TestCase):
    def test_delete_dev_vlans(self):
        if Linux_Server is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=Linux_Server)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=Linux_Server)
        self.assertEqual(del_vlan, 409)

###Hypervisors


#ESX
class Test_Delete_dev_vlans_ESX(TestCase):
    def test_delete_dev_vlans(self):
        if ESX is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=ESX)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=ESX)
        self.assertEqual(del_vlan, 409)


#HyperV
class Test_Delete_dev_vlans_HyperV(TestCase):
    def test_delete_dev_vlans(self):
        if HyperV is None:
            raise SkipTest
        set_vlan = create_dev_vlan(vlanid, vlan_name, auth.creds, auth.url, devip=HyperV)
        del_vlan = delete_dev_vlans(vlanid, auth.creds, auth.url, devip=HyperV)
        self.assertEqual(del_vlan, 409)