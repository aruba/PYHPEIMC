# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.wsm.clientinfo module.

"""

from unittest import TestCase

from pyhpeimc.wsm.clientinfo import *
from test_machine import *


class Test_Get_client_info_all(TestCase):
    def test_get_client_info_all_type(self):
        client = get_client_info_all(auth.creds, auth.url)
        self.assertIs(type(client), list)

    def test_get_client_info_all_content(self):
        clients = get_client_info_all(auth.creds, auth.url)
        self.assertIs(len(clients[0]), 16)
        self.assertIn('ipAddress', clients[0])
        self.assertIn('apLabel', clients[0])
        self.assertIn('apIpAddress', clients[0])
        self.assertIn('acLabel', clients[0])
        self.assertIn('acDevId', clients[0])
        self.assertIn('acIpAddress', clients[0])
        self.assertIn('userName', clients[0])
        self.assertIn('apMacAddress', clients[0])
        self.assertIn('radioType', clients[0])
        self.assertIn('location', clients[0])
        self.assertIn('ssid', clients[0])
        self.assertIn('signalStrength', clients[0])
        self.assertIn('mac', clients[0])
        self.assertIn('upTime', clients[0])
        self.assertIn('apSerialId', clients[0])
        self.assertIn('channel', clients[0])
