#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the system operator
capabilities of the HPE IMC NMS platform using the RESTful API

"""

# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS

# This section deals with HPE IMC Operator Functions



def create_operator(operator, auth, url):
    """
    Function takes input of dictionary operator with the following keys
    operator = { "fullName" : ""   ,
             "sessionTimeout" : "",
             "password" :  "",
             "operatorGroupId" : "",
             "name" : "",
             "desc" : "",
             "defaultAcl" : "",
             "authType"  : ""}
    converts to json and issues a HTTP POST request to the HPE IMC Restful API

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param operator: dictionary with the required operator key-value pairs as defined above.

    :return:

    :rtype:

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.operator import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> operator = { "fullName" : "test administrator",
                     "sessionTimeout" : "30",
                     "password" :  "password",
                     "operatorGroupId" : "1",
                     "name" : "testadmin",
                     "desc" : "test admin account",
                     "defaultAcl" : "",
                     "authType"  : "0"}

    >>> delete_if_exists = delete_plat_operator('testadmin', auth.creds, auth.url)

    >>> new_operator = create_operator(operator, auth.creds, auth.url)

    >>> assert type(new_operator) is int

    >>> assert new_operator == 201

    >>> fail_operator_create = create_operator(operator, auth.creds, auth.url)

    >>> assert type(fail_operator_create) is int

    >>> assert fail_operator_create == 409

    """
    f_url = url + '/imcrs/plat/operator'
    payload = json.dumps(operator, indent=4)
    response = requests.post(f_url, data=payload, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 409:
            return response.status_code
        elif response.status_code == 201:
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' create_operator: An Error has occured'


def set_operator_password(operator, password, auth, url):
    """
    Function to set the password of an existing operator

    :param operator: str Name of the operator account

    :param password: str New password

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: int of 204 if successfull,

    :rtype: int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.operator import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> operator = { "fullName" : "test administrator", "sessionTimeout" : "30",
                     "password" :  "password","operatorGroupId" : "1",
                     "name" : "testadmin","desc" : "test admin account",
                     "defaultAcl" : "","authType"  : "0"}

    >>> new_operator = create_operator(operator, auth.creds, auth.url)

    >>> set_new_password = set_operator_password('testadmin', 'newpassword', auth.creds, auth.url)

    >>> assert type(set_new_password) is int

    >>> assert set_new_password == 204

       """
    if operator is None:
        operator = input(
            '''\n What is the username you wish to change the password?''')
    oper_id = ''
    authtype = None
    plat_oper_list = get_plat_operator(auth, url)
    for i in plat_oper_list:
        if i['name'] == operator:
            oper_id = i['id']
            authtype = i['authType']
    if oper_id == '':
        return "User does not exist"
    change_pw_url = "/imcrs/plat/operator/"
    f_url = url + change_pw_url + oper_id
    if password is None:
        password = input(
            '''\n ============ Please input the operators new password:\n ============  ''')
    payload = json.dumps({'password': password, 'authType': authtype})
    response = requests.put(f_url, data=payload, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            # print("Operator:" + operator +
            # " password was successfully changed")
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' set_operator_password: An Error has occured'


def get_plat_operator(auth, url):
    """
    Funtion takes no inputs and returns a list of dictionaties of all of the operators currently
    configured on the HPE IMC system

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element represents one operator

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.operator import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> plat_operators = get_plat_operator(auth.creds, auth.url)

    >>> assert type(plat_operators) is list

    >>> assert 'name' in plat_operators[0]

    """
    f_url = url + '/imcrs/plat/operator?start=0&size=1000&orderBy=id&desc=false&total=false'
    try:
        response = requests.get(f_url, auth=auth, headers=HEADERS)
        plat_oper_list = json.loads(response.text)['operator']
        if isinstance(plat_oper_list, dict):
            oper_list = [plat_oper_list]
            return oper_list
        return plat_oper_list
    except requests.exceptions.RequestException as error:
        print("Error:\n" + str(error) + ' get_plat_operator: An Error has occured')
        return "Error:\n" + str(error) + ' get_plat_operator: An Error has occured'


def delete_plat_operator(operator, auth, url):
    """
    Function to set the password of an existing operator
    :param operator: str Name of the operator account

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: int of 204 if successfull

    :rtype: int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.operator import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> success_delete_operator = delete_plat_operator('testadmin', auth.creds, auth.url)

    >>> assert type(success_delete_operator) is int

    >>> assert success_delete_operator == 204

    >>> fail_delete_operator = delete_plat_operator('testadmin', auth.creds, auth.url)

    >>> assert type(fail_delete_operator) is int

    >>> assert fail_delete_operator == 409

    """
    oper_id = None
    plat_oper_list = get_plat_operator(auth, url)
    for i in plat_oper_list:
        if operator == i['name']:
            oper_id = i['id']
        else:
            oper_id = None
    if oper_id is None:
        # print ("User does not exist")
        return 409
    f_url = url + "/imcrs/plat/operator/" + str(oper_id)
    response = requests.delete(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 204:
            # print("Operator: " + operator +
            #  " was successfully deleted")
            return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + ' delete_plat_operator: An Error has occured'
