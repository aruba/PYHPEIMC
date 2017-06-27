#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the groups capabilities
of the HPE IMC NMS platform using the RESTful API

"""

import json

import requests

from pyhpeimc.auth import HEADERS




# This section deals with HPE IMC Custom View functions


def get_custom_views(auth, url, name=None):
    """
    function requires no input and returns a list of dictionaries of custom views from an HPE
    IMC. Optional name argument will return only the specified view.
    :param name: str containing the name of the desired custom view

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param name: (optional) str of name of specific custom view

    :return: list of dictionaties containing attributes of the custom views

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.groups import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> all_views = get_custom_views(auth.creds, auth.url)

    >>> assert type(all_views) is list

    >>> assert 'name' in all_views[0]

    >>> non_existant_view = get_custom_views(auth.creds, auth.url, name = '''Doesn't Exist''')

    >>> assert non_existant_view is None


    """
    get_custom_view_url = None
    if name is None:
        get_custom_view_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&desc=false' \
                               '&total=false'
    elif name is not None:
        get_custom_view_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&name=' + \
                               name + '&desc=false&total=false'
    f_url = url + get_custom_view_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            custom_view_list = (json.loads(response.text))
            if 'customView' in custom_view_list:
                custom_view_list = custom_view_list['customView']
                if isinstance(custom_view_list, dict):
                    custom_view_list = [custom_view_list]
                    return custom_view_list
                else:
                    return custom_view_list
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_custom_views: An Error has occured'


def get_custom_view_details(name, auth, url):
    """
    function requires no input and returns a list of dictionaries of custom views from an HPE
    IMC. Optional name argument will return only the specified view.
    :param name: str containing the name of the desired custom view

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param name: (optional) str of name of specific custom view

    :return: list of dictionaties containing attributes of the custom views

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.groups import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> view_details = get_custom_view_details('My Network View', auth.creds, auth.url)

    >>> assert type(view_details) is list

    >>> assert 'label' in view_details[0]

    """
    view_id = get_custom_views(auth, url, name=name)
    if view_id is None:
        return view_id
    view_id = get_custom_views(auth, url, name=name)[0]['symbolId']
    get_custom_view_details_url = '/imcrs/plat/res/view/custom/' + str(view_id)
    f_url = url + get_custom_view_details_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            current_devices = (json.loads(response.text))
            if 'device' in current_devices:
                if isinstance(current_devices['device'], dict):
                    return [current_devices['device']]
                else:
                    return current_devices['device']
            else:
                return []
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_custom_views: An Error has occured'


def create_custom_views(auth, url, name=None, upperview=None):
    """
    function takes no input and issues a RESTFUL call to get a list of custom views from HPE IMC.
    Optional Name input will return only the specified view.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param name: string containg the name of the desired custom view

    :param upperview: str contraining the name of the desired parent custom view

    :return: str of creation results ( "view " + name + "created successfully"

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.groups import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    #Create L1 custom view
    >>> create_custom_views(auth.creds, auth.url, name='L1 View')
    'View L1 View created successfully'

    >>> view_1 =get_custom_views( auth.creds, auth.url, name = 'L1 View')

    >>> assert type(view_1) is list

    >>> assert view_1[0]['name'] == 'L1 View'

    #Create Nested custome view
    >>> create_custom_views(auth.creds, auth.url, name='L2 View', upperview='L1 View')
    'View L2 View created successfully'

    >>> view_2 = get_custom_views( auth.creds, auth.url, name = 'L2 View')

    >>> assert type(view_2) is list

    >>> assert view_2[0]['name'] == 'L2 View'

    """
    create_custom_views_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&desc=false' \
                               '&total=false'
    f_url = url + create_custom_views_url
    if upperview is None:
        payload = '''{ "name": "''' + name + '''",
         "upLevelSymbolId" : ""}'''
    else:
        parentviewid = get_custom_views(auth, url, upperview)[0]['symbolId']
        payload = '''{ "name": "''' + name + '''",
        "upLevelSymbolId" : "''' + str(parentviewid) + '''"}'''
    response = requests.post(f_url, data=payload, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 201:
            print('View ' + name + ' created successfully')
            return response.status_code
        elif response.status_code == 409:
            print("View " + name + " already exists")
            return response.status_code
        else:
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_custom_views: An Error has occured'




def add_devs_custom_views(custom_view_name, dev_list, auth, url):
    """
    function takes a list of devIDs from devices discovered in the HPE IMC platform and issues a
    RESTFUL call to add the list of devices to a specific custom views from HPE IMC.

    :param custom_view_name: str of the target custom view name

    :param dev_list: list containing the devID of all devices to be contained in this custom view.

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str of creation results ( "view " + name + "created successfully"

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    """
    view_id = get_custom_views(auth, url, name=custom_view_name)
    if view_id is None:
        print("View " + custom_view_name + " doesn't exist")
        return view_id
    view_id = get_custom_views(auth, url, name=custom_view_name)[0]['symbolId']
    add_devs_custom_views_url = '/imcrs/plat/res/view/custom/' + str(view_id)
    device_list = []
    for dev in dev_list:
        new_dev = {"id": dev}
        device_list.append(new_dev)
    payload = '''{"device" : ''' + json.dumps(device_list) + '''}'''
    print(payload)
    f_url = url + add_devs_custom_views_url
    response = requests.put(f_url, data=payload, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            print('View ' + custom_view_name + ' : Devices Successfully Added')
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' get_custom_views: An Error has occured'


def delete_custom_view(auth, url, name):
    """
    function takes input of auth, url, and name and issues a RESTFUL call to delete a specific
    of custom views from HPE
    IMC.
    :param name: string containg the name of the desired custom view

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: str of creation results ( "view " + name + "created successfully"

    :rtype: str

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.groups import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> delete_custom_view(auth.creds, auth.url, name = "L1 View")
    'View L1 View deleted successfully'

    >>> view_1 =get_custom_views( auth.creds, auth.url, name = 'L1 View')

    >>> assert view_1 is None

    >>> delete_custom_view(auth.creds, auth.url, name = "L2 View")
    'View L2 View deleted successfully'

    >>> view_2 =get_custom_views( auth.creds, auth.url, name = 'L2 View')

    >>> assert view_2 is None

    """
    view_id = get_custom_views(auth, url, name)
    if view_id is None:
        print("View " + name + " doesn't exists")
        return view_id
    view_id = get_custom_views(auth, url, name)[0]['symbolId']
    delete_custom_view_url = '/imcrs/plat/res/view/custom/' + str(view_id)
    f_url = url + delete_custom_view_url
    response = requests.delete(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            print('View ' + name + ' deleted successfully')
            return response.status_code
        else:
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' delete_custom_view: An Error has occured'
