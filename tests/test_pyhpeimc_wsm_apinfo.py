# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.wsm.apinfo module.

"""

import ipaddress
from unittest import TestCase


from pyhpeimc.wsm.apinfo import *
from test_machine import *


# test for get_ac_info_all
class Test_Get_get_ap_info_all(TestCase):
    def test_get_ap_info_all_type(self):
        aps = get_ap_info_all(auth.creds, auth.url)
        self.assertIs(type(aps), list)

    def test_get_ac_info_all_type(self):
        aps = get_ap_info_all(auth.creds, auth.url)
        self.assertIs(len(aps[0]), 19)
        self.assertIn('ipAddress', aps[0])
        self.assertIn('ssids', aps[0])
        self.assertIn('isFit', aps[0])
        self.assertIn('onlineClientCount', aps[0])
        self.assertIn('hardwareVersion', aps[0])
        self.assertIn('label', aps[0])
        self.assertIn('serialId', aps[0])
        self.assertIn('sysName', aps[0])
        self.assertIn('acDevId', aps[0])
        self.assertIn('onlineStatus', aps[0])
        self.assertIn('connectType', aps[0])
        self.assertIn('status', aps[0])
        self.assertIn('type', aps[0])
        self.assertIn('location', aps[0])
        self.assertIn('acIpAddress', aps[0])
        self.assertIn('macAddress', aps[0])
        self.assertIn('apAlias', aps[0])
        self.assertIn('acLabel', aps[0])
        self.assertIn('softwareVersion', aps[0])


# test for get_ac_info_all

class Test_Get_ap_info(TestCase):
    def test_get_ap_info_all_type(self):
        aps = get_ap_info_all(auth.creds, auth.url)
        ip = ''
        for ap in aps:
            try:
                ip = ipaddress.ip_address(ap['ipAddress'])
                break
            except:
                continue
        ap = get_ap_info(ip, auth.creds, auth.url)
        self.assertIs(type(ap), dict)

    def test_get_ap_info_all_content(self):
        aps = get_ap_info_all(auth.creds, auth.url)
        ip = ''
        for ap in aps:
            try:
                ip = ipaddress.ip_address(ap['ipAddress'])
                break
            except:
                continue
        ap = get_ap_info(ip, auth.creds, auth.url)
        #self.assertIs(len(ap), 20)
        self.assertIn('ipAddress', ap)
        self.assertIn('ssids', ap)
        self.assertIn('isFit', ap)
        #self.assertIn('locationList', ap)
        self.assertIn('onlineClientCount', ap)
        self.assertIn('hardwareVersion', ap)
        self.assertIn('label', ap)
        self.assertIn('serialId', ap)
        self.assertIn('sysName', ap)
        self.assertIn('acDevId', ap)
        self.assertIn('onlineStatus', ap)
        self.assertIn('connectType', ap)
        self.assertIn('status', ap)
        self.assertIn('type', ap)
        self.assertIn('location', ap)
        self.assertIn('acIpAddress', ap)
        self.assertIn('macAddress', ap)
        self.assertIn('apAlias', ap)
        self.assertIn('acLabel', ap)
        self.assertIn('softwareVersion', ap)
