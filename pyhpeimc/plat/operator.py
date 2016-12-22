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

HEADERS = {'Accept': 'application/json', 'Content-Type':
           'application/json', 'Accept-encoding': 'application/json'}

"""
This section deals with HPE IMC Operator Functions
"""


def create_operator(operator, auth, url, headers=HEADERS):
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

    :param headers: json formated string. default values set in module

    :return:

    :rtype:


    >>> import json

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
    create_operator_url = '/imcrs/plat/operator'
    f_url = url + create_operator_url
    payload = json.dumps(operator, indent=4)
    # creates the URL using the payload variable as the contents
    r = requests.post(f_url, data=payload, auth=auth, headers=headers)
    try:
        if r.status_code == 409:
            return r.status_code
        elif r.status_code == 201:
            return r.status_code
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + ' create_operator: An Error has occured'


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

    >>> operator = '''{ "fullName" : "test administrator", "sessionTimeout" : "30","password" :  "password","operatorGroupId" : "1","name" : "testadmin","desc" : "test admin account","defaultAcl" : "","authType"  : "0"}'''

    >>> operator = json.loads(operator)

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
    r = requests.put(f_url, data=payload, auth=auth, headers=HEADERS)
    try:
        if r.status_code == 204:
            # print("Operator:" + operator +
            # " password was successfully changed")
            return r.status_code
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + ' set_operator_password: An Error has occured'


def get_plat_operator(auth, url):
    """
    Funtion takes no inputs and returns a list of dictionaties of all of the operators currently configured on the HPE
    IMC system

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
    get_operator_url = '/imcrs/plat/operator?start=0&size=1000&orderBy=id&desc=false&total=false'
    f_url = url + get_operator_url
    try:
        r = requests.get(f_url, auth=auth, headers=HEADERS)
        plat_oper_list = json.loads(r.text)['operator']
        if type(plat_oper_list) is dict:
            oper_list = [plat_oper_list]
            return oper_list
        return plat_oper_list
    except requests.exceptions.RequestException as e:
        print("Error:\n" + str(e) + ' get_plat_operator: An Error has occured')
        return "Error:\n" + str(e) + ' get_plat_operator: An Error has occured'


def delete_plat_operator(operator, auth, url, headers=HEADERS):
    """
    Function to set the password of an existing operator
    :param operator: str Name of the operator account

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param headers: json formated string. default values set in module

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
    delete_plat_operator_url = "/imcrs/plat/operator/"
    f_url = url + delete_plat_operator_url + str(oper_id)
    r = requests.delete(f_url, auth=auth, headers=headers)
    try:
        if r.status_code == 204:
            # print("Operator: " + operator +
            #  " was successfully deleted")
            return r.status_code
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + ' delete_plat_operator: An Error has occured'
