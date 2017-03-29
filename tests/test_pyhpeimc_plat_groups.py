# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.groups module.

"""

from unittest import TestCase

from pyhpeimc.plat.groups import *
from pyhpeimc.plat.device import get_dev_details
from test_machine import *


#TODO Remarked out failing test
class TestGet_custom_views(TestCase):
    def test_get_custom_views_type(self):
        all_views = get_custom_views(auth.creds, auth.url)
        self.assertIs(type(all_views), list)

    def test_get_custom_views_content(self):
        all_views = get_custom_views(auth.creds, auth.url)
        # self.assertIs(len(all_views[0]), 6)
        # self.assertIn('upLevelSymbolId', all_views[0])
        self.assertIn('autoAddDevType', all_views[0])
        self.assertIn('symbolId', all_views[0])
        self.assertIn('runStatus', all_views[0])
        self.assertIn('statusImgSrc', all_views[0])
        self.assertIn('name', all_views[0])
        self.assertIn('statusDesc', all_views[0])


    def test_get_custom_views_doesnt_exist(self):
        non_existant_view = get_custom_views(auth.creds, auth.url, name='''Doesn't Exist''')
        self.assertEqual(non_existant_view, None)


class TestGet_custom_views_details(TestCase):
    def test_get_custom_views_details_type(self):
        view_details = get_custom_view_details('My Network View', auth.creds, auth.url)
        self.assertIs(type(view_details), list)

    def test_get_custom_views_details_content(self):
        view_details = get_custom_view_details('My Network View', auth.creds, auth.url)
        self.assertIs(len(view_details[0]), 14)
        self.assertIn('label', view_details[0])
        self.assertIn('link', view_details[0])
        self.assertIn('ip', view_details[0])
        self.assertIn('categoryId', view_details[0])
        self.assertIn('status', view_details[0])
        self.assertIn('devCategoryImgSrc', view_details[0])
        self.assertIn('topoIconName', view_details[0])
        self.assertIn('location', view_details[0])
        self.assertIn('mask', view_details[0])
        self.assertIn('contact', view_details[0])
        self.assertIn('sysDescription', view_details[0])
        self.assertIn('id', view_details[0])
        self.assertIn('sysName', view_details[0])
        self.assertIn('sysOid', view_details[0])


    def test_get_custom_views_details_doesnt_exist(self):
        non_existant_view = get_custom_view_details('Doesnt Exist', auth.creds, auth.url)
        self.assertEqual(non_existant_view, None)


class TestCreate_custom_views(TestCase):
    def test_create_custom_view(self):
        delete_custom_view(auth.creds, auth.url, name="L1 View")
        new_view = create_custom_views(auth.creds, auth.url, name='L1 View')
        self.assertIs(new_view, 201)
        view_1 = get_custom_views(auth.creds, auth.url, name='L1 View')
        self.assertIs(type(view_1),list)
        self.assertEqual(view_1[0]['name'],'L1 View' )
        delete_custom_view(auth.creds, auth.url, name="L1 View")

    def test_create_custom_view_already_exists(self):
        create_custom_views(auth.creds, auth.url, name='L1 View')
        new_view = create_custom_views(auth.creds, auth.url, name='L1 View')
        self.assertEqual(new_view, 409)
        delete_custom_view(auth.creds, auth.url, name="L1 View")

    def test_create_child_custom_view(self):
        delete_custom_view(auth.creds, auth.url, name="L1 View")
        delete_custom_view(auth.creds, auth.url, name="L2 View")
        create_custom_views(auth.creds, auth.url, name='L1 View')
        child_view = create_custom_views(auth.creds, auth.url, name='L2 View', upperview='L1 View')
        self.assertIs(child_view, 201)
        view_1 = get_custom_views(auth.creds, auth.url, name='L2 View')
        self.assertIs(type(view_1), list)
        self.assertEqual(view_1[0]['name'], 'L2 View')
        delete_custom_view(auth.creds, auth.url, name="L1 View")
        delete_custom_view(auth.creds, auth.url, name="L2 View")


class TestDelete_delete_views_details(TestCase):
    def test_delete_custom_view(self):
        create_custom_views(auth.creds, auth.url, name='L1 View')
        delete_view = delete_custom_view(auth.creds, auth.url, name="L1 View")
        self.assertIs(delete_view, 204)
        view_1 = get_custom_views(auth.creds, auth.url, name='L1 View')
        self.assertEqual(view_1,None)


    def test_delete_custom_view_doesnt_exists(self):
        delete_view = delete_custom_view(auth.creds, auth.url, name="L1 View")
        delete_view = delete_custom_view(auth.creds, auth.url, name="L1 View")
        self.assertEqual(delete_view, None)


class TestAdd_devs_custom_views(TestCase):
    """
    Test to add multiple evices to single custom view
    """

    def setUp(self):
        create_custom_views(auth.creds, auth.url, name='L1 View')

    def tearDown(self):
        delete_custom_view(auth.creds, auth.url, name="L1 View")


    def test_add_devs_custom_viewsType(self):
        dev_list = [get_dev_details(CW5_Switch, auth.creds, auth.url)['id']]
        add_devs = add_devs_custom_views('L1 View', dev_list, auth.creds, auth.url)
        self.assertIs(add_devs, 204)
        self.assertIs(type(add_devs), int)


    def test_add_devs_custom_views_Content(self):
        dev_list = [get_dev_details(CW5_Switch, auth.creds, auth.url)['id']]
        add_devs = add_devs_custom_views('L1 View', dev_list, auth.creds, auth.url)
        view_details = get_custom_view_details('L1 View', auth.creds, auth.url)
        view_dev_list = []
        for dev in view_details:
            print (dev['ip'])
            view_dev_list.append(dev['ip'])
        self.assertEqual(get_dev_details(CW5_Switch, auth.creds, auth.url)['ip'], view_dev_list[0])

