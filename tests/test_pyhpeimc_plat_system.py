# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.system module.

"""

from unittest import TestCase

from pyhpeimc.plat.system import *
from test_machine import auth


class TestGet_system_vendors(TestCase):
    def test_get_system_vendors_type(self):
        vendors = get_system_vendors(auth.creds, auth.url)
        self.assertIs(type(vendors), list)

    def test_get_system_vendors_content(self):
        vendors = get_system_vendors(auth.creds, auth.url)
        self.assertIs(len(vendors[0]), 8)
        self.assertIn('link', vendors[0])
        self.assertIn('preDefined', vendors[0])
        self.assertIn('name', vendors[0])
        self.assertIn('contact', vendors[0])
        self.assertIn('iconId', vendors[0])
        self.assertIn('id', vendors[0])
        self.assertIn('description', vendors[0])
        self.assertIn('phone', vendors[0])


# get_system_category
class TestGet_system_category(TestCase):
    def testGet_system_category_type(self):
        categories = get_system_category(auth.creds, auth.url)
        self.assertIs(type(categories), list)

    def testGet_system_category_content(self):
        categories = get_system_category(auth.creds, auth.url)
        self.assertIs(len(categories[0]), 9)
        self.assertIn('link', categories[0])
        self.assertIn('topoIconId', categories[0])
        self.assertIn('preDefined', categories[0])
        self.assertIn('name', categories[0])
        self.assertIn('iconId', categories[0])
        self.assertIn('id', categories[0])
        self.assertIn('isDefaultDisplay', categories[0])
        self.assertIn('displayId', categories[0])
        self.assertIn('priority', categories[0])


# get_system_device_models
class TestGet_system_device_models(TestCase):
    def test_get_system_device_models_type(self):
        device_models = get_system_device_models(auth.creds, auth.url)
        self.assertIs(type(device_models), list)

    def test_get_system_device_models_content(self):
        device_models = get_system_device_models(auth.creds, auth.url)
        self.assertIs(len(device_models[0]), 14)
        self.assertIn('sysOid', device_models[0])
        self.assertIn('preDefined', device_models[0])
        self.assertIn('name', device_models[0])
        self.assertIn('categoryId', device_models[0])
        self.assertIn('defaultTopoIconId', device_models[0])
        self.assertIn('deviceVersion', device_models[0])
        self.assertIn('description', device_models[0])
        self.assertIn('defaultIconId', device_models[0])
        self.assertIn('seriesId', device_models[0])
        self.assertIn('dfield', device_models[0])
        self.assertIn('link', device_models[0])
        self.assertIn('id', device_models[0])
        self.assertIn('virtualDeviceName', device_models[0])
        self.assertIn('applicationName', device_models[0])


# get_system_series
class TestGet_system_series(TestCase):
    def test_get_system_series_type(self):
        series = get_system_series(auth.creds, auth.url)
        self.assertIs(type(series), list)

    def test_get_system_series_content(self):
        series = get_system_series(auth.creds, auth.url)
        self.assertIs(len(series[0]), 6)
        self.assertIn('link', series[0])
        self.assertIn('preDefined', series[0])
        self.assertIn('name', series[0])
        self.assertIn('id', series[0])
        self.assertIn('vendorId', series[0])
        self.assertIn('description', series[0])


# Section deals with device authentication templates. Get and Set functions available apply to
# IMC 7.3 and later

class TestGet_Telnet_Template(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_telnet_template_type(self):
        """Test to ensure that the return of get_telnet_template is a list"""
        template = get_telnet_template(auth.creds, auth.url)
        self.assertIs(type(template), list)

    def test_get_telnet_template_content(self):
        """
        Test to ensure the attributes of the get_telnet_template are consistent between versions
        :return:
        """
        template = get_telnet_template(auth.creds, auth.url)
        self.assertIn('id', template[0])
        self.assertIn('type', template[0])
        self.assertIn('name', template[0])
        self.assertIn('authType', template[0])
        self.assertIn('userName', template[0])
        self.assertIn('userPassword', template[0])
        self.assertIn('superPassword', template[0])
        self.assertIn('authTypeStr', template[0])
        self.assertIn('timeout', template[0])
        self.assertIn('retries', template[0])
        self.assertIn('port', template[0])
        self.assertIn('version', template[0])
        self.assertIn('creator', template[0])
        self.assertIn('accessType', template[0])
        self.assertIn('operatorGroupStr', template[0])
        self.assertIn('link', template[0])


    def test_get_exist_template(self):
        """
        test to ensure get existing template returns proper object
        """
        template = get_telnet_template(auth.creds, auth.url, template_name="default")
        self.assertEqual(template[0]['name'], 'default')
        self.assertEqual(template[0]['port'], '23')
        self.assertEqual(template[0]['creator'], 'admin')


    def test_fail_non_exist_template(self):
        """
        test to ensure get non-existing template returns proper object
        """
        template = get_telnet_template(auth.creds, auth.url, template_name="not_there")
        self.assertEqual(template, 404)


class TestCreateTelnetTemplate(TestCase):
    """
    Class to test create_telnet_template functions
    """

    def setUp(self):
        pass


    def tearDown(self):
        delete_telnet_template(auth.creds, auth.url, "User_with_Enable")

    def test_create_telnet_template(self):
        template = {
            "type": "0",
            "name": "User_with_Enable",
            "authType": "3",
            "userName": "",
            "userPassword": "password",
            "superPassword": "password",
            "authTypeStr": "Password + Super/Manager Password (No Operator)",
            "timeout": "4",
            "retries": "1",
            "port": "23",
            "version": "1",
            "creator": "admin",
            "accessType": "1",
            "operatorGroupStr": ""
            }
        output = create_telnet_template(auth.creds, auth.url, template)
        self.assertEqual(output, 201)

    def test_fail_create_existing_tempalte(self):
        """
        Test to ensure can't create the same telnet template twice
        :return: integer of 404
        rtype int
        """
        template = {
            "type": "0",
            "name": "User_with_Enable",
            "authType": "3",
            "userName": "",
            "userPassword": "password",
            "superPassword": "password",
            "authTypeStr": "Password + Super/Manager Password (No Operator)",
            "timeout": "4",
            "retries": "1",
            "port": "23",
            "version": "1",
            "creator": "admin",
            "accessType": "1",
            "operatorGroupStr": ""
        }
        output = create_telnet_template(auth.creds, auth.url, template)
        output = create_telnet_template(auth.creds, auth.url, template)
        #self.assertEqual(output, my_values)

class TestDeleteTelnetTemplate(TestCase):
    """
    Tests for delete_telnet_template function
    """

    def setUp(self):
        template = {
            "type": "0",
            "name": "User_with_Enable",
            "authType": "3",
            "userName": "",
            "userPassword": "password",
            "superPassword": "password",
            "authTypeStr": "Password + Super/Manager Password (No Operator)",
            "timeout": "4",
            "retries": "1",
            "port": "23",
            "version": "1",
            "creator": "admin",
            "accessType": "1",
            "operatorGroupStr": ""
        }
        output = create_telnet_template(auth.creds, auth.url, template)

    def tearDown(self):
        pass

    def test_delete_existing_template(self):
        output = delete_telnet_template(auth.creds, auth.url, "User_with_Enable")
        self.assertEqual(output, 204)

