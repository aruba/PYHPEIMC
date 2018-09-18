# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.operator module.

"""

from unittest import TestCase

from pyhpeimc.plat.operator import *
from test_machine import *


class TestCreate_operator(TestCase):
    def test_create_operator(self):
        operator = '''{ "fullName" : "test administrator", "sessionTimeout" : "30","password" :  "password","operatorGroupId" : "1","name" : "testadmin","desc" : "test admin account","defaultAcl" : "","authType"  : "0"}'''
        operator = json.loads(operator)
        delete_if_exists = delete_plat_operator('testadmin', auth.creds, auth.url)
        new_operator = create_operator(operator, auth.creds, auth.url)
        self.assertIs(type(new_operator), int)
        self.assertEqual(new_operator, 201)
        delete_plat_operator('testadmin', auth.creds, auth.url)

    def test_create_operator_already_exists(self):
        operator = '''{ "fullName" : "test administrator", "sessionTimeout" : "30","password" :  "password","operatorGroupId" : "1","name" : "testadmin","desc" : "test admin account","defaultAcl" : "","authType"  : "0"}'''
        operator = json.loads(operator)
        delete_if_exists = delete_plat_operator('testadmin', auth.creds, auth.url)
        new_operator = create_operator(operator, auth.creds, auth.url)
        new_operator = create_operator(operator, auth.creds, auth.url)
        self.assertIs(type(new_operator), int)
        self.assertEqual(new_operator, 409)
        delete_plat_operator('testadmin', auth.creds, auth.url)


class TestSet_operator_password(TestCase):
    def test_set_operator_password(self):
        operator = '''{ "fullName" : "test administrator", "sessionTimeout" : "30","password" :  "password","operatorGroupId" : "1","name" : "testadmin","desc" : "test admin account","defaultAcl" : "","authType"  : "0"}'''
        operator = json.loads(operator)
        delete_if_exists = delete_plat_operator('testadmin', auth.creds, auth.url)
        new_operator = create_operator(operator, auth.creds, auth.url)
        set_new_password = set_operator_password('testadmin', 'newpassword', auth.creds, auth.url)
        self.assertIs(type(new_operator), int)
        self.assertEqual(new_operator, 201)
        delete_plat_operator('testadmin', auth.creds, auth.url)

    def test_set_operator_password_doesnt_exists(self):
        delete_if_exists = delete_plat_operator('testadmin', auth.creds, auth.url)
        set_new_password = set_operator_password('testadmin', 'newpassword', auth.creds, auth.url)
        self.assertIs(type(set_new_password), str)
        self.assertEqual(set_new_password, "User does not exist")
        delete_plat_operator('testadmin', auth.creds, auth.url)


class TestGet_plat_operator(TestCase):
    def test_get_plat_operator_type(self):
        plat_operators = get_plat_operator(auth.creds, auth.url)
        self.assertIs(type(plat_operators), list)

    def test_get_plat_operator_content(self):
        plat_operators = get_plat_operator(auth.creds, auth.url)
        self.assertIs(len(plat_operators[0]), 12)
        self.assertIn('name',plat_operators[0])
        self.assertIn('defaultManagedDefinedView', plat_operators[0])
        self.assertIn('id', plat_operators[0])
        self.assertIn('authType', plat_operators[0])
        self.assertIn('defaultManagedGroup', plat_operators[0])
        self.assertIn('link', plat_operators[0])
        self.assertIn('desc', plat_operators[0])
        self.assertIn('operatorGroupId', plat_operators[0])
        self.assertIn('fullName', plat_operators[0])


class TestDelete_plat_operator(TestCase):
    def test_delete_plat_operator(self):
        operator = '''{ "fullName" : "test administrator", "sessionTimeout" : "30","password" :  "password","operatorGroupId" : "1","name" : "testadmin","desc" : "test admin account","defaultAcl" : "","authType"  : "0"}'''
        operator = json.loads(operator)
        delete_if_exists = delete_plat_operator('testadmin', auth.creds, auth.url)
        new_operator = create_operator(operator, auth.creds, auth.url)
        delete_operator = delete_plat_operator('testadmin', auth.creds, auth.url)
        self.assertIs(type(delete_operator), int)
        self.assertEqual(delete_operator, 204)


    def test_delete_plat_operator_doesnt_exists(self):
        delete_if_exists = delete_plat_operator('testadmin', auth.creds, auth.url)
        delete_dont_exist = delete_plat_operator('testadmin', auth.creds, auth.url)
        self.assertIs(type(delete_dont_exist), int)
        self.assertEqual(delete_dont_exist, 409)
