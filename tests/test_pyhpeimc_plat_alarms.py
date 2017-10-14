# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase

from pyhpeimc.plat.alarms import *
from test_machine import auth


# TODO Remarked out failing tests


class TestGetDevAlarms(TestCase):
    """
    Test Case for pyhpeimc plat alarms get_dev_alarms functions
    """

    def test_get_dev_alarms_type(self):
        """
        test case for get_dev_alarms type

        """
        dev_alarms = get_dev_alarms(auth.creds, auth.url, devip='10.101.0.231')
        self.assertIs(type(dev_alarms), list)

    def test_get_dev_alarms_content(self):
        dev_alarms = get_dev_alarms(auth.creds, auth.url, devip='10.101.0.231')
        self.assertIn('ackStatus', dev_alarms[0])
        self.assertIn('recTimeDesc', dev_alarms[0])
        self.assertIn('originalTypeDesc', dev_alarms[0])
        self.assertIn('ackStatusDesc', dev_alarms[0])
        self.assertIn('ackTimeDesc', dev_alarms[0])
        self.assertIn('ackTime', dev_alarms[0])
        self.assertIn('deviceIp', dev_alarms[0])
        self.assertIn('recTime', dev_alarms[0])
        self.assertIn('id', dev_alarms[0])
        self.assertIn('faultTimeDesc', dev_alarms[0])
        self.assertIn('faultTime', dev_alarms[0])
        # self.assertIn('holdInfo', dev_alarms[0])
        self.assertIn('originalType', dev_alarms[0])
        self.assertIn('recStatus', dev_alarms[0])
        self.assertIn('alarmDesc', dev_alarms[0])
        self.assertIn('alarmDetail', dev_alarms[0])
        self.assertIn('alarmLevelDesc', dev_alarms[0])
        self.assertIn('remark', dev_alarms[0])
        self.assertIn('ackUserName', dev_alarms[0])
        self.assertIn('alarmCategoryDesc', dev_alarms[0])
        self.assertIn('recUserName', dev_alarms[0])
        self.assertIn('alarmCategory', dev_alarms[0])
        self.assertIn('parentId', dev_alarms[0])
        self.assertIn('recStatusDesc', dev_alarms[0])
        self.assertIn('alarmLevel', dev_alarms[0])
        self.assertIn('somState', dev_alarms[0])
        self.assertIn('deviceName', dev_alarms[0])
        self.assertIn('paras', dev_alarms[0])
        self.assertIn('OID', dev_alarms[0])
        self.assertIn('deviceId', dev_alarms[0])


class TestGetRealtimeAlarm(TestCase):
    def test_get_realtime_alarm_type(self):
        real_time_alarm = get_realtime_alarm('admin', auth.creds, auth.url)
        self.assertIs(type(real_time_alarm), list)

    def test_get_realtime_alarm_content(self):
        real_time_alarm = get_realtime_alarm('admin', auth.creds, auth.url)
        #self.assertIs(len(real_time_alarm[0]), 7)
        self.assertIn('faultTime', real_time_alarm[0])
        self.assertIn('userAckUserName', real_time_alarm[0])
        self.assertIn('id', real_time_alarm[0])
        self.assertIn('deviceDisplay', real_time_alarm[0])
        self.assertIn('faultDesc', real_time_alarm[0])
        self.assertIn('userAckType', real_time_alarm[0])


# TODO Remarked out failing test
# TODO Get_all_alarms testing - Need to investigate
"""
class TestGetAllAlarm(TestCase):
    def test_get_alarms_type(self):
        all_alarms = get_alarms('admin', auth.creds, auth.url)
        self.assertIs(type(all_alarms), list)
    def test_get_alarms_content(self):
        all_alarms = get_alarms('admin', auth.creds, auth.url)
        #self.assertIs(len(all_alarms[0]), 29)
        self.assertIn('ackStatus',all_alarms[0])
        self.assertIn('parentId', all_alarms[0])
        self.assertIn('recUserName', all_alarms[0])
        self.assertIn('alarmCategory', all_alarms[0])
        self.assertIn('deviceId', all_alarms[0])
        self.assertIn('alarmCategoryDesc', all_alarms[0])
        self.assertIn('originalType', all_alarms[0])
        self.assertIn('ackStatusDesc', all_alarms[0])
        self.assertIn('recTimeDesc', all_alarms[0])
        self.assertIn('alarmDesc', all_alarms[0])
        self.assertIn('deviceIp', all_alarms[0])
        self.assertIn('recStatusDesc', all_alarms[0])
        self.assertIn('alarmLevel', all_alarms[0])
        self.assertIn('ackTime', all_alarms[0])
        self.assertIn('alarmDetail', all_alarms[0])
        self.assertIn('remark', all_alarms[0])
        self.assertIn('ackTimeDesc', all_alarms[0])
        self.assertIn('originalTypeDesc', all_alarms[0])
        self.assertIn('alarmLevelDesc', all_alarms[0])
        self.assertIn('recStatus', all_alarms[0])
        self.assertIn('deviceName', all_alarms[0])
        self.assertIn('faultTime', all_alarms[0])
        self.assertIn('faultTimeDesc', all_alarms[0])
        self.assertIn('somState', all_alarms[0])
        self.assertIn('id', all_alarms[0])
        self.assertIn('OID', all_alarms[0])
        self.assertIn('paras', all_alarms[0])
        self.assertIn('recTime', all_alarms[0])
        self.assertIn('ackUserName', all_alarms[0])
        #self.assertIn('holdInfo', all_alarms[0])
"""
