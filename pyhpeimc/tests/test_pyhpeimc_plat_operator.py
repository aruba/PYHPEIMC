from unittest import TestCase
from nose.plugins.skip import Skip, SkipTest
from pyhpeimc.tests.test_machine import *
from pyhpeimc.plat.operator import *

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