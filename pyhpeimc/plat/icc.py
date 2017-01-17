#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the icc (configuration
management) capabilities of the HPE IMC NMS platform using the RESTful API

"""

# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS


def get_cfg_template(auth, url, folder=None):
    """
    Function takes no input and returns a list of dictionaries containing the configuration
    templates in the root folder of the icc configuration template library.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param folder: optional str of name of target folder

    :folder = str of target folder name

    :return: List of Dictionaries containing folders and configuration files in the ICC library.

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> config_templates = get_cfg_template(auth.creds, auth.url)

    >>> assert type(config_templates) is list

    >>> assert 'confFileName' in config_templates[0]


    >>> config_templates_folder = get_cfg_template(auth.creds, auth.url, folder='ADP_Configs')

    >>> assert type(config_templates_folder) is list

    >>> assert 'confFileName' in config_templates_folder[0]

    >>> config_template_no_folder = get_cfg_template(auth.creds, auth.url, folder='Doesnt_Exist')

    >>> assert config_template_no_folder is None
    """
    if folder is None:
        get_cfg_template_url = "/imcrs/icc/confFile/list"
    else:
        folder_id = get_folder_id(folder, auth, url)
        get_cfg_template_url = "/imcrs/icc/confFile/list/" + str(folder_id)
    f_url = url + get_cfg_template_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            cfg_template_list = (json.loads(response.text))
            return cfg_template_list['confFile']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_cfg_template: An Error has occured"


def create_cfg_segment(filename, filecontent, description, auth, url):
    """
    Takes a str into var filecontent which represents the entire content of a configuration
    segment, or partial configuration file. Takes a str into var description which represents the
    description of the configuration segment
    :param filename: str containing the name of the configuration segment.

    :param filecontent: str containing the entire contents of the configuration segment

    :param description: str contrianing the description of the configuration segment

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: If successful, Boolena of type True

    :rtype: Boolean

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> filecontent = 'sample file content'

    >>> create_new_file = create_cfg_segment('CW7SNMP.cfg',
                                              filecontent,
                                              'My New Template',
                                               auth.creds,
                                               auth.url)

    >>> template_id = get_template_id('CW7SNMP.cfg', auth.creds, auth.url)

    >>> assert type(template_id) is str

    >>>
    """
    payload = {"confFileName": filename,
               "confFileType": "2",
               "cfgFileParent": "-1",
               "confFileDesc": description,
               "content": filecontent}
    f_url = url + "/imcrs/icc/confFile"
    response = requests.post(f_url, data=(json.dumps(payload)), auth=auth, headers=HEADERS)
    try:
        if response.status_code == 201:
            print("Template successfully created")
            return response.status_code
        elif response.status_code is not 201:
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " create_cfg_segment: An Error has occured"


def get_template_id(template_name, auth, url):
    """
    Helper function takes str input of folder name and returns str numerical id of the folder.
    :param template_name: str name of the target template

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str numerical id of the folder

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> file_id = get_template_id('CW7SNMP.cfg', auth.creds, auth.url)

    >>> assert type(file_id) is int

    """
    object_list = get_cfg_template(auth=auth, url=url)
    for template in object_list:
        if template['confFileName'] == template_name:
            return int(template['confFileId'])
    return "template not found"


def get_folder_id(folder_name, auth, url):
    """
    Helper function takes str input of folder name and returns str numerical id of the folder.
    :param folder_name: str name of the folder

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str numerical id of the folder

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> default_folder_id = get_folder_id('Default Folder', auth.creds, auth.url)

    >>> assert type(default_folder_id) is int

    """
    object_list = get_cfg_template(auth=auth, url=url)
    for template in object_list:
        if template['confFileName'] == folder_name:
            return int(template['confFileId'])
    return "Folder not found"


def delete_cfg_template(template_name, auth, url):
    """Uses the get_template_id() funct to gather the template_id
    to craft a url which is sent to the IMC server using a Delete Method
    :param template_name: str containing the entire contents of the configuration segment

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: If successful, return int of status.code 204.

    :rtype: Int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> delete_cfg_template('CW7SNMP.cfg', auth.creds, auth.url)


    """
    file_id = get_template_id(template_name, auth, url)
    f_url = url + "/imcrs/icc/confFile/" + str(file_id)
    response = requests.delete(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            print("Template successfully Deleted")
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " delete_cfg_template: An Error has occured"


def get_template_details(template_name, auth, url):
    """Uses the get_template_id() funct to gather the template_id to craft a
    get_template_details_url which is sent to the IMC server using
    a get Method
    :param template_name: str containing the entire contents of the configuration segment

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: If successful, return dict containing the template details

    :rtype: dict

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.icc import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> filecontent = 'sample file content'

    >>> create_new_file = create_cfg_segment('CW7SNMP.cfg',
                                              filecontent,
                                              'My New Template',
                                               auth.creds,
                                               auth.url)

    >>> template_contents = get_template_details('CW7SNMP.cfg', auth.creds, auth.url)

    >>> assert type(template_contents) is dict

    """
    file_id = get_template_id(template_name, auth, url)
    if isinstance(file_id, str):
        return file_id
    f_url = url + "/imcrs/icc/confFile/" + str(file_id)
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            template_details = json.loads(response.text)
            return template_details
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_template_contents: An Error has occured"
