# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.vrm module.

"""


from unittest import TestCase
from nose.plugins.skip import SkipTest
from pyhpeimc.tests.test_machine import *
from pyhpeimc.plat.vrm import *



#####Test get_vm_host_info for Multiple Vendor Devices


#ESX
class Test_Get_dev_vlans_ESX(TestCase):
    def test_get_dev_vlans_type(self):
        if ESX is None:
            raise SkipTest
        host = get_vm_host_info(ESX, auth.creds, auth.url)
        self.assertIs(type(host), dict)

    def test_get_dev_vlans_content(self):
        if ESX is None:
            raise SkipTest
        host = get_vm_host_info(ESX, auth.creds, auth.url)
        self.assertIs(len(host), 10)
        self.assertIn('cpuNum', host)
        self.assertIn('porductFlag', host)
        self.assertIn('memory', host)
        self.assertIn('devIp', host)
        self.assertIn('devId', host)
        self.assertIn('vendor', host)
        self.assertIn('cpuFeg', host)
        self.assertIn('parentDevId', host)
        self.assertIn('serverName', host)
        self.assertIn('diskSize', host)


#HyperV
class Test_Get_dev_vlans_HyperV(TestCase):
    def test_get_dev_vlans_type(self):
        if HyperV is None:
            raise SkipTest
        host = get_vm_host_info(HyperV, auth.creds, auth.url)
        self.assertIs(type(host), dict)

    def test_get_dev_vlans_type(self):
        if HyperV is None:
            raise SkipTest
        host = get_vm_host_info(HyperV, auth.creds, auth.url)
        self.assertIs(len(host), 10)
        self.assertIn('cpuNum', host)
        self.assertIn('porductFlag', host)
        self.assertIn('memory', host)
        self.assertIn('devIp', host)
        self.assertIn('devId', host)
        self.assertIn('vendor', host)
        self.assertIn('cpuFeg', host)
        self.assertIn('parentDevId', host)
        self.assertIn('serverName', host)
        self.assertIn('diskSize', host)


#####Test get_vm_host_vnic for Multiple Vendor Devices


#ESX
class Test_Get_vm_host_vnicESX(TestCase):
    def test_get_vm_host_vnic_type(self):
        if ESX is None:
            raise SkipTest
        host = get_vm_host_vnic(ESX, auth.creds, auth.url)
        self.assertIs(type(host), dict)

    def test_get_vm_host_vnic_type(self):
        if ESX is None:
            raise SkipTest
        host = get_vm_host_vnic(ESX, auth.creds, auth.url)
        self.assertIs(len(host), 8)
        self.assertIn('vSwtichKey', host[0])
        self.assertIn('mask', host[0])
        self.assertIn('vSwitchName', host[0])
        self.assertIn('serverDevId', host[0])
        self.assertIn('ip', host[0])
        self.assertIn('nicName', host[0])


#HyperV
class Test_Get_vm_host_vnicHyperV(TestCase):
    def test_get_vm_host_vnic_type(self):
        if HyperV is None:
            raise SkipTest
        host = get_vm_host_vnic(HyperV, auth.creds, auth.url)
        self.assertIs(type(host), dict)

    def test_get_vm_host_vnic_type(self):
        if HyperV is None:
            raise SkipTest
        host = get_vm_host_vnic(HyperV, auth.creds, auth.url)
        self.assertIs(len(host), 8)
        self.assertIn('vSwtichKey', host[0])
        self.assertIn('mask', host[0])
        self.assertIn('vSwitchName', host[0])
        self.assertIn('serverDevId', host[0])
        self.assertIn('ip', host[0])
        self.assertIn('nicName', host[0])


#####Test get_host_vms for Multiple Vendor Devices


#ESX
class Test_Get_host_vmsESX(TestCase):
    def test_get_vm_host_vnic_type(self):
        if ESX is None:
            raise SkipTest
        vms = get_host_vms(ESX, auth.creds, auth.url)
        self.assertIs(type(vms), list)

    def test_get_host_vms_type(self):
        if ESX is None:
            raise SkipTest
        vms = get_host_vms(ESX, auth.creds, auth.url)
        self.assertIs(len(vms), 16)
        self.assertIn('vmIP', vms[0])
        self.assertIn('memory', vms[0])
        self.assertIn('osDesc', vms[0])
        self.assertIn('powerState', vms[0])
        self.assertIn('vmTools', vms[0])
        self.assertIn('parentServerId', vms[0])
        self.assertIn('porductFlag', vms[0])
        self.assertIn('vmName', vms[0])
        self.assertIn('cpu', vms[0])
        self.assertIn('vmDevId', vms[0])
        self.assertIn('vmMask', vms[0])
        self.assertIn('coresPerCpu', vms[0])


#HyperV
class Test_Get_host_vmsHyperV(TestCase):
    def test_get_vm_host_vnic_type(self):
        if HyperV is None:
            raise SkipTest
        vms = get_host_vms(HyperV, auth.creds, auth.url)
        self.assertIs(type(vms), list)

    def test_get_host_vms_type(self):
        if HyperV is None:
            raise SkipTest
        vms = get_host_vms(HyperV, auth.creds, auth.url)
        self.assertIs(len(vms), 16)
        self.assertIn('vmIP', vms[0])
        self.assertIn('memory', vms[0])
        self.assertIn('osDesc', vms[0])
        self.assertIn('powerState', vms[0])
        self.assertIn('vmTools', vms[0])
        self.assertIn('parentServerId', vms[0])
        self.assertIn('porductFlag', vms[0])
        self.assertIn('vmName', vms[0])
        self.assertIn('cpu', vms[0])
        self.assertIn('vmDevId', vms[0])
        self.assertIn('vmMask', vms[0])
        self.assertIn('coresPerCpu', vms[0])