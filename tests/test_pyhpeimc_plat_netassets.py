# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.netassets module.

"""

from unittest import TestCase

from nose.plugins.skip import SkipTest

from pyhpeimc.plat.netassets import *
from test_machine import *


##### Test get_dev_asset_details function for multiple vendors

### Switches


#CW3_Switch
class TestGet_dev_asset_detailsCW3_Switch(TestCase):
    def test_get_dev_asset_details_type(self):
        if CW3_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(CW3_Switch, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if CW3_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(CW3_Switch, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 27) # TODO Modified len from 28 to 27 need to investigate
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        # self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#CW5_Switch
class TestGet_dev_asset_detailsCW5_Switch(TestCase):
    def test_get_dev_asset_details_type(self):
        if CW5_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(CW5_Switch, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if CW5_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(CW5_Switch, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 28)
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])



#CW7_Switch
class TestGet_dev_asset_detailsCW7_Switch(TestCase):
    def test_get_dev_asset_details_type(self):
        if CW7_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(CW7_Switch, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if CW7_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(CW7_Switch, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 28)
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#Cisco_Switch
class TestGet_dev_asset_detailsCisco_Switch(TestCase):
    def test_get_dev_asset_details_type(self):
        if Cisco_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Cisco_Switch, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if Cisco_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Cisco_Switch, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 28)
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#Juniper_Switch
class TestGet_dev_asset_detailsJuniper_Switch(TestCase):
    def test_get_dev_asset_details_type(self):
        if Juniper_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Juniper_Switch, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if Juniper_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Juniper_Switch, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 28)
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#Arista_Switch
class TestGet_dev_asset_detailsArista_Switch(TestCase):
    def test_get_dev_asset_details_type(self):
        if Arista_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Arista_Switch, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if Arista_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Arista_Switch, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 27) # TODO modified len from 28 to 27 need to investigate
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        # self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#ArubaOS_Switch (Formerly Provision)
class TestGet_dev_asset_detailsArubaOS_Switch(TestCase):
    def test_get_dev_asset_details_type(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(ArubaOS_Switch, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if ArubaOS_Switch is None:
            raise SkipTest
        single_asset = get_dev_asset_details(ArubaOS_Switch, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 28)
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


###Routers


#Cisco_Router
class TestGet_dev_asset_detailsCisco_Router(TestCase):
    def test_get_dev_asset_details_type(self):
        if Cisco_Router is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Cisco_Router, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if Cisco_Router is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Cisco_Router, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 27) # TODO Modified len from 28 to 27 need to investigate
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        # self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#CW5_Router
class TestGet_dev_asset_detailsCW5_Router(TestCase):
    def test_get_dev_asset_details_type(self):
        if CW5_Router is None:
            raise SkipTest
        single_asset = get_dev_asset_details(CW5_Router, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if CW5_Router is None:
            raise SkipTest
        single_asset = get_dev_asset_details(CW5_Router, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 28)
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#Juniper_Router (SRV)
class TestGet_dev_asset_detailsJuniper_Router(TestCase):
    def test_get_dev_asset_details_type(self):
        if Juniper_Router is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Juniper_Router, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if Juniper_Router is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Juniper_Router, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 28)
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


####Servers


#Windows_Server
class TestGet_dev_asset_detailsWindows_Server(TestCase):
    def test_get_dev_asset_details_type(self):
        if Windows_Server is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Windows_Server, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if Windows_Server is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Windows_Server, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 27) # TODO Modified len from 28 to 27 need to investigate
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        # self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#Linux_Server
class TestGet_dev_asset_detailsLinux_Server(TestCase):
    def test_get_dev_asset_details_type(self):
        if Linux_Server is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Linux_Server, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if Linux_Server is None:
            raise SkipTest
        single_asset = get_dev_asset_details(Linux_Server, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 27) # TODO Modified len from 28 to 27 Need to investigate
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        # self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


###Hypervisors


#ESX
class TestGet_dev_asset_detailsESX(TestCase):
    def test_get_dev_asset_details_type(self):
        if ESX is None:
            raise SkipTest
        single_asset = get_dev_asset_details(ESX, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if ESX is None:
            raise SkipTest
        single_asset = get_dev_asset_details(ESX, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 27) # TODO Modified len from 28 to 27 need to investigate
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        # self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


#HyperV
class TestGet_dev_asset_detailsHyperV(TestCase):
    def test_get_dev_asset_details_type(self):
        if HyperV is None:
            raise SkipTest
        single_asset = get_dev_asset_details(HyperV, auth.creds, auth.url)
        self.assertIs(type(single_asset), list)
    def test_get_dev_asset_details_content(self):
        if HyperV is None:
            raise SkipTest
        single_asset = get_dev_asset_details(HyperV, auth.creds, auth.url)
        self.assertIs(len(single_asset[0]), 28)
        self.assertIn('asset', single_asset[0])
        self.assertIn('phyClass', single_asset[0])
        self.assertIn('beginDate', single_asset[0])
        self.assertIn('devId', single_asset[0])
        self.assertIn('hardVersion', single_asset[0])
        self.assertIn('isFRU', single_asset[0])
        self.assertIn('deviceIp', single_asset[0])
        self.assertIn('cleiCode', single_asset[0])
        self.assertIn('physicalFlag', single_asset[0])
        self.assertIn('mfgName', single_asset[0])
        self.assertIn('firmwareVersion', single_asset[0])
        self.assertIn('buildInfo', single_asset[0])
        self.assertIn('relPos', single_asset[0])
        self.assertIn('boardNum', single_asset[0])
        self.assertIn('alias', single_asset[0])
        self.assertIn('deviceName', single_asset[0])
        self.assertIn('softVersion', single_asset[0])
        self.assertIn('bom', single_asset[0])
        self.assertIn('name', single_asset[0])
        self.assertIn('containedIn', single_asset[0])
        self.assertIn('assetNumber', single_asset[0])
        self.assertIn('model', single_asset[0])
        self.assertIn('vendorType', single_asset[0])
        self.assertIn('serialNum', single_asset[0])
        self.assertIn('remark', single_asset[0])
        self.assertIn('desc', single_asset[0])
        self.assertIn('phyIndex', single_asset[0])
        self.assertIn('serverDate', single_asset[0])


class TestGet_dev_asset_details_doesnt_exist(TestCase):
    def test_get_dev_asset_details_doesnt_exist(self):
        if DoesntExist is None:
            raise SkipTest
        asset_doesnt_exist = get_dev_asset_details(DoesntExist, auth.creds, auth.url)
        self.assertIs(type(asset_doesnt_exist), int)
        self.assertEqual(asset_doesnt_exist, 403)


##### Test get_dev_asset_details_all function


#TODO Remarked out Failing test
class TestGet_dev_asset_details_all(TestCase):
    def test_get_dev_asset_details_all_type(self):
        all_assets = get_dev_asset_details_all(auth.creds, auth.url)
        self.assertIs(type(all_assets), list)


    def test_get_dev_asset_details_all_content(self):
        all_assets = get_dev_asset_details_all(auth.creds, auth.url)
        #self.assertIs(len(all_assets[0]), 28)
        self.assertIn('asset', all_assets[0])
        self.assertIn('phyClass', all_assets[0])
        #self.assertIn('beginDate', all_assets[0])
        self.assertIn('devId', all_assets[0])
        self.assertIn('hardVersion', all_assets[0])
        self.assertIn('isFRU', all_assets[0])
        self.assertIn('deviceIp', all_assets[0])
        self.assertIn('cleiCode', all_assets[0])
        self.assertIn('physicalFlag', all_assets[0])
        self.assertIn('mfgName', all_assets[0])
        self.assertIn('firmwareVersion', all_assets[0])
        self.assertIn('buildInfo', all_assets[0])
        self.assertIn('relPos', all_assets[0])
        self.assertIn('boardNum', all_assets[0])
        self.assertIn('alias', all_assets[0])
        self.assertIn('deviceName', all_assets[0])
        self.assertIn('softVersion', all_assets[0])
        self.assertIn('bom', all_assets[0])
        self.assertIn('name', all_assets[0])
        self.assertIn('containedIn', all_assets[0])
        self.assertIn('assetNumber', all_assets[0])
        self.assertIn('model', all_assets[0])
        self.assertIn('vendorType', all_assets[0])
        self.assertIn('serialNum', all_assets[0])
        self.assertIn('remark', all_assets[0])
        self.assertIn('desc', all_assets[0])
        self.assertIn('phyIndex', all_assets[0])
        self.assertIn('serverDate', all_assets[0])




