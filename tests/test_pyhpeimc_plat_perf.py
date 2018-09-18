# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.perf module.

"""

from unittest import TestCase

from pyhpeimc.plat.perf import *
from test_machine import *


class TestAdd_perf_task(TestCase):
    def test_add_perf_task(self):
        delete_task = delete_perf_task('Test_Task', auth.creds, auth.url)
        new_task = {'indexDesc': '1.3.6.1.4.1.9.9.13.1.3.1.3',
                    'indexType': '[index1[0]:ciscoEnvMonTemperatureStatusValue:1:0]',
                    'itemFunction': '1.3.6.1.4.1.9.9.13.1.3.1.3', 'itemName': 'Test_Task',
                    'selectDefaultUnit': '400', 'unit': 'Celsius'}

        new_perf_task = add_perf_task(new_task, auth.creds, auth.url)
        self.assertIs(type(new_perf_task), int)
        self.assertEqual(new_perf_task, 204)
        delete_task = delete_perf_task('Test_Task', auth.creds, auth.url)


    def test_add_perf_task_already_exists(self):
        new_task = {'indexDesc': '1.3.6.1.4.1.9.9.13.1.3.1.3',
                    'indexType': '[index1[0]:ciscoEnvMonTemperatureStatusValue:1:0]',
                    'itemFunction': '1.3.6.1.4.1.9.9.13.1.3.1.3', 'itemName': 'Test_Task',
                    'selectDefaultUnit': '400', 'unit': 'Celsius'}

        new_perf_task = add_perf_task(new_task, auth.creds, auth.url)
        new_perf_task = add_perf_task(new_task, auth.creds, auth.url)
        self.assertIs(type(new_perf_task), int)
        self.assertEqual(new_perf_task, 404)
        delete_task = delete_perf_task('Test_Task', auth.creds, auth.url)


class TestGet_perf_task(TestCase):
    def test_get_perf_task_type(self):
        new_task = {'indexDesc': '1.3.6.1.4.1.9.9.13.1.3.1.3',
                    'indexType': '[index1[0]:ciscoEnvMonTemperatureStatusValue:1:0]',
                    'itemFunction': '1.3.6.1.4.1.9.9.13.1.3.1.3', 'itemName': 'Test_Task',
                    'selectDefaultUnit': '400', 'unit': 'Celsius'}

        new_perf_task = add_perf_task(new_task, auth.creds, auth.url)
        task_details = get_perf_task("Test_Task", auth.creds, auth.url)
        self.assertIs(type(task_details), dict)
        self.assertEqual(task_details['taskDescr'], "Test_Task")
        delete_task = delete_perf_task('Test_Task', auth.creds, auth.url)

    def test_get_perf_task_content(self):
        new_task = {'indexDesc': '1.3.6.1.4.1.9.9.13.1.3.1.3',
                    'indexType': '[index1[0]:ciscoEnvMonTemperatureStatusValue:1:0]',
                    'itemFunction': '1.3.6.1.4.1.9.9.13.1.3.1.3', 'itemName': 'Test_Task',
                    'selectDefaultUnit': '400', 'unit': 'Celsius'}

        new_perf_task = add_perf_task(new_task, auth.creds, auth.url)
        task_details = get_perf_task("Test_Task", auth.creds, auth.url)
        self.assertIs(len(task_details), 25)
        self.assertIn('alarmTwoTimes', task_details)
        self.assertIn('taskName', task_details)
        self.assertIn('alarmTwoMode', task_details)
        self.assertIn('enableAlterTwo', task_details)
        self.assertIn('alarmTwoThresholdSecond', task_details)
        self.assertIn('alarmOneTimes', task_details)
        self.assertIn('perfTemplate', task_details)
        self.assertIn('alarmOneLevel', task_details)
        self.assertIn('componentID', task_details)
        self.assertIn('taskId', task_details)
        self.assertIn('alarmOneThresholdFirst', task_details)
        self.assertIn('tempId', task_details)
        self.assertIn('alarmOneMode', task_details)
        self.assertIn('sumId', task_details)
        self.assertIn('taskDescr', task_details)
        self.assertIn('alarmTwoThresholdFirst', task_details)
        self.assertIn('tempUnit', task_details)
        self.assertIn('groupId', task_details)
        self.assertIn('collectInterval', task_details)
        self.assertIn('unitId', task_details)
        self.assertIn('alarmOneThresholdSecond', task_details)
        self.assertIn('tempUnitDependList', task_details)
        self.assertIn('enableAlterOne', task_details)
        delete_task = delete_perf_task('Test_Task', auth.creds, auth.url)


    def test_get_perf_task_doesnt_exist(self):
        task_details = get_perf_task("doesnt_exist", auth.creds, auth.url)
        self.assertIs(type(task_details), str)
        self.assertEqual("Task Doesn't Exist", task_details)


class TestDelete_perf_task(TestCase):
    def test_delete_perf_task(self):
        new_task = {'indexDesc': '1.3.6.1.4.1.9.9.13.1.3.1.3',
                    'indexType': '[index1[0]:ciscoEnvMonTemperatureStatusValue:1:0]',
                    'itemFunction': '1.3.6.1.4.1.9.9.13.1.3.1.3', 'itemName': 'Test_Task',
                    'selectDefaultUnit': '400', 'unit': 'Celsius'}

        new_perf_task = add_perf_task(new_task, auth.creds, auth.url)
        delete_task = delete_perf_task('Test_Task', auth.creds, auth.url)
        self.assertIs(type(delete_task), int)
        self.assertIs(delete_task, 204)

    def test_delete_perf_task(self):
        delete_task = delete_perf_task('doesnt_exist', auth.creds, auth.url)
        self.assertIs(type(delete_task), int)
        self.assertEqual(delete_task, 403)






