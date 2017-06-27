# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.icc module.

"""

from unittest import TestCase

from pyhpeimc.plat.icc import *
from test_machine import *


#TODO remarked out failing test
class TestGet_cfg_template(TestCase):
    def test_get_cfg_template_type(self):
        config_templates = get_cfg_template(auth.creds, auth.url)
        self.assertIs(type(config_templates), list)

    def test_get_cfg_template_content(self):
            config_templates = get_cfg_template(auth.creds, auth.url)
            self.assertIs(len(config_templates[0]), 13)
            self.assertIn('syncType',config_templates[0])
            self.assertIn('confFileDesc', config_templates[0])
            self.assertIn('confFileName', config_templates[0])
            self.assertIn('createBy', config_templates[0])
            self.assertIn('cfgFileParent', config_templates[0])
            self.assertIn('confFileId', config_templates[0])
            self.assertIn('appliedDevices', config_templates[0])
            self.assertIn('defaultConfFile', config_templates[0])
            self.assertIn('confFilePath', config_templates[0])
            self.assertIn('modifyAt', config_templates[0])
            self.assertIn('createAt', config_templates[0])
            self.assertIn('defaultConfFileDesc', config_templates[0])

    def test_get_cfg_template_folder_type(self):
            config_templates_folder = get_cfg_template(auth.creds, auth.url, folder='Default '
                                                                                    'Folder')
            self.assertIs(type(config_templates_folder), list)

    def test_get_cfg_templates_folder_content(self):
            config_templates_folder = get_cfg_template(auth.creds, auth.url, folder='Default '
                                                                                    'Folder')
            self.assertIs(len(config_templates_folder[0]), 13)
            self.assertIn('syncType', config_templates_folder[0])
            self.assertIn('confFileDesc', config_templates_folder[0])
            self.assertIn('confFileName', config_templates_folder[0])
            self.assertIn('createBy', config_templates_folder[0])
            self.assertIn('cfgFileParent', config_templates_folder[0])
            self.assertIn('confFileId', config_templates_folder[0])
            self.assertIn('appliedDevices', config_templates_folder[0])
            self.assertIn('defaultConfFile', config_templates_folder[0])
            self.assertIn('confFilePath', config_templates_folder[0])
            #self.assertIn('modifyAt', config_templates_folder[0])
            self.assertIn('createAt', config_templates_folder[0])
            self.assertIn('defaultConfFileDesc', config_templates_folder[0])

    def test_get_cfg_templates_no_folder(self):
        config_template_no_folder = get_cfg_template(auth.creds, auth.url, folder='Doesnt_Exist')
        self.assertEqual(config_template_no_folder, None)


class TestCreate_cfg_segment(TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)

    def test_create_cfg_segment_type(self):
        filecontent = ("""sample file content""")
        create_new_file = create_cfg_segment('CW7SNMP.cfg', filecontent, 'My New Template',
                                             auth.creds, auth.url)
        self.assertIs(type(create_new_file), int)



class TestGet_template_id(TestCase):
    def setUp(self):
        filecontent = ("""sample file content""")
        create_cfg_segment('CW7SNMP.cfg', filecontent, 'My New Template', auth.creds, auth.url)

    def tearDown(self):
        delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)

    def test_get_template_id(self):
        file_id = get_template_id('CW7SNMP.cfg', auth.creds, auth.url)
        self.assertIs(type(file_id), int)

    def test_get_template_id_doesnt_exist(self):
        file_id = get_template_id('Notthere.cfg', auth.creds, auth.url)
        self.assertIs(type(file_id), str)
        self.assertEqual(file_id, 'template not found')


class TestGet_folder_id(TestCase):
    def test_get_folder_id(self):
        default_folder_id = get_folder_id('Default Folder', auth.creds, auth.url)
        self.assertIs(type(default_folder_id), int)


    def test_get_folder_id_doesnt_exist(self):
        doesntexist_folder = get_folder_id('Doesnt Exist Folder', auth.creds, auth.url)
        self.assertIs(type(doesntexist_folder), str)
        self.assertEqual(doesntexist_folder, 'Folder not found')

class TestDelete_cfg_template(TestCase):
    def test_delete_cfg_template(self):
        filecontent = ("""sample file content""")
        create_new_file = create_cfg_segment('CW7SNMP.cfg', filecontent, 'My New Template', auth.creds, auth.url)
        delete_cfg_template_result = delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)
        self.assertIs(type(delete_cfg_template_result), int)
        self.assertIs(delete_cfg_template_result, 204)

class TestGet_template_contents(TestCase):
    def test_get_template_details_type(self):
        delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)
        filecontent = ("""sample file content""")
        create_new_file = create_cfg_segment('CW7SNMP.cfg', filecontent, 'My New Template', auth.creds, auth.url)
        template_contents = get_template_details('CW7SNMP.cfg', auth.creds, auth.url)
        self.assertIs(type(template_contents), dict)
        delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)

    def test_get_template_details_content(self):
        delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)
        filecontent = ("""sample file content""")
        create_new_file = create_cfg_segment('CW7SNMP.cfg', filecontent, 'My New Template', auth.creds, auth.url)
        template_contents = get_template_details('CW7SNMP.cfg', auth.creds, auth.url)
        self.assertIs(len(template_contents), 14)
        self.assertIn('confFileName', template_contents)
        self.assertIn('confFileTypeDesc', template_contents)
        self.assertIn('cfgFileParent', template_contents)
        self.assertIn('confFileDesc', template_contents)
        self.assertIn('createBy', template_contents)
        self.assertIn('appliedDevices', template_contents)
        self.assertIn('confFileType', template_contents)
        self.assertIn('content', template_contents)
        self.assertIn('defaultConfFile', template_contents)
        self.assertIn('createAt', template_contents)
        self.assertIn('confFileId', template_contents)
        self.assertIn('defaultConfFileDesc', template_contents)
        self.assertIn('syncType', template_contents)
        self.assertIn('confFilePath', template_contents)
        self.assertEqual(filecontent, template_contents['content'])
        delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)







