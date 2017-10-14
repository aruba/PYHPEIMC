# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.wsm.acinfo module.

"""

from unittest import TestCase

from test_machine import *

from pyhpeimc.wsm.acinfo import *


# test for get_ac_info_all

class Test_Get_ac_info_all(TestCase):
    def test_get_ac_info_all_type(self):
        acs = get_ac_info_all(auth.creds, auth.url)
        self.assertIs(type(acs), list)

    def test_get_ac_info_all_content(self):
        acs = get_ac_info_all(auth.creds, auth.url)
        #self.assertIs(len(acs[0]), 12)
        self.assertIn('ipAddress', acs[0])
        self.assertIn('pingStatus', acs[0])
        self.assertIn('onlineClientCount', acs[0])
        self.assertIn('hardwareVersion', acs[0])
        self.assertIn('label', acs[0])
        self.assertIn('serialId', acs[0])
        self.assertIn('macAddress', acs[0])
        self.assertIn('status', acs[0])
        self.assertIn('type', acs[0])
        self.assertIn('onlineApCount', acs[0])
        self.assertIn('sysName', acs[0])
        self.assertIn('softwareVersion', acs[0])
