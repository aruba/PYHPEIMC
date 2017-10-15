#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for working with the system configuration
capabilities of the HPE IMC NMS platform using the RESTful API

"""


# This section imports required libraries
import json

import requests

from pyhpeimc.auth import HEADERS


# This section contains functions which operate at the system level


def get_system_vendors(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single vendor

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.system import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> vendors = get_system_vendors(auth.creds, auth.url)

      >>> assert type(vendors) is list

      >>> assert 'name' in vendors[0]


    """
    f_url = url + '/imcrs/plat/res/vendor?start=0&size=10000&orderBy=id&desc=false&total=false'
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            system_vendors = (json.loads(response.text))
            return system_vendors['deviceVendor']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_details: An Error has occured"


def get_system_category(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC\n

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device category

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> categories = get_system_category(auth.creds, auth.url)

      >>> assert type(categories) is list

      >>> assert 'name' in categories[0]


    """
    f_url = url + '/imcrs/plat/res/category?start=0&size=10000&orderBy=id&desc=false&total=false'
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            system_category = (json.loads(response.text))
            return system_category['deviceCategory']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_details: An Error has occured"


def get_system_device_models(auth, url):
    """Takes string no input to issue RESTUL call to HP IMC

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device model

      :rtype: list


      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> device_models = get_system_device_models(auth.creds, auth.url)

      >>> assert type(device_models) is list

      >>> assert 'virtualDeviceName' in device_models[0]

    """
    f_url = url + '/imcrs/plat/res/model?start=0&size=10000&orderBy=id&desc=false&total=false'
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            system_device_model = (json.loads(response.text))
            return system_device_model['deviceModel']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_details: An Error has occured"


def get_system_series(auth, url):
    """Takes no input to issue RESTUL call to HP IMC

      :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

      :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

      :return: list of dictionaries where each dictionary represents a single device series

      :rtype: list

      >>> from pyhpeimc.auth import *

      >>> from pyhpeimc.plat.device import *

      >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

      >>> series = get_system_series(auth.creds, auth.url)

      >>> assert type(series) is list

      >>> assert 'name' in series[0]

    """
    f_url = url + '/imcrs/plat/res/series?managedOnly=false&start=0&size=10000&orderBy=id&desc' \
                   '=false&total=false'
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            system_series = (json.loads(response.text))
            return system_series['deviceSeries']
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_dev_series: An Error has occured"

# This section deals with manipulating system authentication credentials

# Telnet Templates

def create_telnet_template(auth, url, telnet_template ):
    """
    Function takes input of a dictionry containing the required key/value pair for the creation
    of a telnet template.

    :param auth:
    :param url:
    :param telnet_template: dictionary of valid JSON which complains to API schema
    :return: int value of HTTP response code 201 for proper creation or 404 for failed creation
    :rtype int

    Sample of proper KV pairs. Please see documentation for valid values for different fields.

    telnet_template = {"type": "0",
    "name": "User_with_Enable",
    "authType": "4",
    "userName": "admin",
    "userPassword": "password",
    "superPassword": "password",
    "authTypeStr": "Username + Password + Super/Manager Password",
    "timeout": "4",
    "retries": "1",
    "port": "23",
    "version": "1",
    "creator": "admin",
    "accessType": "1",
    "operatorGroupStr": ""}
    """
    f_url = url + "/imcrs/plat/res/telnet/add"
    response = requests.post(f_url, data = json.dumps(telnet_template), auth=auth, headers=HEADERS)
    try:
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " create_telnet_template: An Error has occured"

def get_telnet_template(auth, url, template_name=None):
    """
    Takes no input, or template_name as input to issue RESTUL call to HP IMC

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param template_name: str value of template name

    :return list object containing one or more dictionaries where each dictionary represents one
    telnet template

    :rtype list

    """
    f_url = url + "/imcrs/plat/res/telnet?start=0&size=10000&desc=false&total=false"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            telnet_templates = (json.loads(response.text))
            template = None
            if type(telnet_templates['telnetParamTemplate']) is dict:
                my_templates = [telnet_templates['telnetParamTemplate']]
                telnet_templates['telnetParamTemplate'] = my_templates
            if template_name is None:
                return telnet_templates['telnetParamTemplate']
            elif template_name is not None:
                for telnet_template in telnet_templates['telnetParamTemplate']:

                    if telnet_template['name'] == template_name:
                        template = [telnet_template]
                print (type(template))
                if template == None:
                    return 404
                else:
                    return template
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_telnet_templates: An Error has occured"


def modify_telnet_template(auth, url, telnet_template, template_name= None, template_id = None):
    """
    Function takes input of a dictionry containing the required key/value pair for the modification
    of a telnet template.

    :param auth:
    :param url:
    :param telnet_template: Human readable label which is the name of the specific telnet template
    :param template_id Internal IMC number which designates the specific telnet template
    :return: int value of HTTP response code 201 for proper creation or 404 for failed creation
    :rtype int

    Sample of proper KV pairs. Please see documentation for valid values for different fields.

    telnet_template = {"type": "0",
    "name": "User_with_Enable",
    "authType": "4",
    "userName": "newadmin",
    "userPassword": "newpassword",
    "superPassword": "newpassword",
    "authTypeStr": "Username + Password + Super/Manager Password",
    "timeout": "4",
    "retries": "1",
    "port": "23",
    "version": "1",
    "creator": "admin",
    "accessType": "1",
    "operatorGroupStr": ""}
    """
    if template_name is None:
        template_name = telnet_template['name']
    if template_id is None:
        telnet_templates = get_telnet_template(auth, url)
        template_id = None
        for template in telnet_templates:
            if template['name'] == template_name:
                template_id = template['id']
    f_url = url + "/imcrs/plat/res/telnet/"+str(template_id)+"/update"
    response = requests.put(f_url, data = json.dumps(telnet_template), auth=auth, headers=HEADERS)
    try:
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " modify_telnet_template: An Error has occured"


def delete_telnet_template(auth, url, template_name= None, template_id= None):
    """
    Takes template_name as input to issue RESTUL call to HP IMC which will delete the specific
    telnet template from the IMC system

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param template_name: str value of template name

    :param template_id: str value template template_id value

    :return: int HTTP response code

    :rtype  int
    """
    try:
        if template_id is None:
            telnet_templates = get_telnet_template(auth, url)
            if template_name is None:
                template_name = telnet_template['name']
            template_id = None
            for template in telnet_templates:
                if template['name'] == template_name:
                    template_id = template['id']
        f_url = url + "/imcrs/plat/res/telnet/%s/delete" % template_id
        response = requests.delete(f_url, auth=auth, headers=HEADERS)
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " delete_telnet_template: An Error has occured"


# SSH Templates

def create_ssh_template(auth, url, ssh_template ):
    """
    Function takes input of a dictionry containing the required key/value pair for the creation
    of a ssh template.

    :param auth:
    :param url:
    :param ssh: dictionary of valid JSON which complains to API schema
    :return: int value of HTTP response code 201 for proper creation or 404 for failed creation
    :rtype int

    Sample of proper KV pairs. Please see documentation for valid values for different fields.

    ssh_template = {
    "type": "0",
    "name": "ssh_admin_template",
    "authType": "3",
    "authTypeStr": "Password + Super Password",
    "userName": "admin",
    "password": "password",
    "superPassword": "password",
    "port": "22",
    "timeout": "10",
    "retries": "3",
    "keyFileName": "",
    "keyPhrase": ""
    }
    """
    f_url = url + "/imcrs/plat/res/ssh/add"
    response = requests.post(f_url, data = json.dumps(ssh_template), auth=auth, headers=HEADERS)
    try:
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " create_ssh_template: An Error has occured"

def get_ssh_template(auth, url, template_name=None):
    """
    Takes no input, or template_name as input to issue RESTUL call to HP IMC

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param template_name: str value of template name

    :return list object containing one or more dictionaries where each dictionary represents one
    ssh template

    :rtype list

    """
    f_url = url + "/imcrs/plat/res/ssh?start=0&size=10000&desc=false&total=false"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            ssh_templates = (json.loads(response.text))
            template = None
            if type(ssh_templates['sshParamTemplate']) is dict:
                my_templates = [ssh_templates['sshParamTemplate']]
                ssh_templates['sshParamTemplate'] = my_templates
            if template_name is None:
                return ssh_templates['sshParamTemplate']
            elif template_name is not None:
                for ssh_template in ssh_templates['sshParamTemplate']:
                    if ssh_template['name'] == template_name:
                        template = [ssh_template]
                print (type(template))
                if template == None:
                    return 404
                else:
                    return template
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_ssh_templates: An Error has occured"


def modify_ssh_template(auth, url, ssh_template, template_name= None, template_id = None):
    """
    Function takes input of a dictionry containing the required key/value pair for the modification
    of a ssh template.

    :param auth:
    :param url:
    :param ssh_template: Human readable label which is the name of the specific ssh template
    :param template_id Internal IMC number which designates the specific ssh template
    :return: int value of HTTP response code 201 for proper creation or 404 for failed creation
    :rtype int

    Sample of proper KV pairs. Please see documentation for valid values for different fields.

    ssh_template = {
    "type": "0",
    "name": "ssh_admin_template",
    "authType": "3",
    "authTypeStr": "Password + Super Password",
    "userName": "newadmin",
    "password": "password",
    "superPassword": "password",
    "port": "22",
    "timeout": "10",
    "retries": "3",
    "keyFileName": "",
    "keyPhrase": ""
    }
    """
    if template_name is None:
        template_name = ssh_template['name']
    if template_id is None:
        ssh_templates = get_ssh_template(auth, url)
        template_id = None
        for template in ssh_templates:
            if template['name'] == template_name:
                template_id = template['id']
    f_url = url + "/imcrs/plat/res/ssh/"+str(template_id)+"/update"
    response = requests.put(f_url, data = json.dumps(ssh_template), auth=auth, headers=HEADERS)
    try:
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " modify_ssh_template: An Error has occured"


def delete_ssh_template(auth, url, template_name= None, template_id= None):
    """
    Takes template_name as input to issue RESTUL call to HP IMC which will delete the specific
    ssh template from the IMC system

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param template_name: str value of template name

    :param template_id: str value template template_id value

    :return: int HTTP response code

    :rtype  int
    """
    try:
        if template_id is None:
            ssh_templates = get_ssh_template(auth, url)
            if template_name is None:
                template_name = ssh_template['name']
            template_id = None
            for template in ssh_templates:
                if template['name'] == template_name:
                    template_id = template['id']
        f_url = url + "/imcrs/plat/res/ssh/%s/delete" % template_id
        response = requests.delete(f_url, auth=auth, headers=HEADERS)
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " delete_ssh_template: An Error has occured"












# snmp Templates

def create_snmp_template(auth, url, snmp_template ):
    """
    Function takes input of a dictionry containing the required key/value pair for the creation
    of a snmp template.

    :param auth:
    :param url:
    :param ssh: dictionary of valid JSON which complains to API schema
    :return: int value of HTTP response code 201 for proper creation or 404 for failed creation
    :rtype int

    Sample of proper KV pairs. Please see documentation for valid values for different fields.

    snmp_template =  {
      "version": "2",
      "name": "new_snmp_template",
      "type": "0",
      "paraType": "SNMPv2c",
      "roCommunity": "public",
      "rwCommunity": "private",
      "timeout": "4",
      "retries": "3",
      "contextName": "",
      "securityName": " ",
      "securityMode": "1",
      "authScheme": "0",
      "authPassword": "",
      "privScheme": "0",
      "privPassword": "",
      "snmpPort": "161",
      "isAutodiscoverTemp": "1",
      "creator": "admin",
      "accessType": "1",
      "operatorGroupStr": ""
      }
    """
    f_url = url + "/imcrs/plat/res/snmp/add"
    response = requests.post(f_url, data = json.dumps(snmp_template), auth=auth, headers=HEADERS)
    try:
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " create_snmp_template: An Error has occured"

def get_snmp_templates(auth, url, template_name=None):
    """
    Takes no input, or template_name as input to issue RESTUL call to HP IMC

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param template_name: str value of template name

    :return list object containing one or more dictionaries where each dictionary represents one
    snmp template

    :rtype list

    """
    f_url = url + "/imcrs/plat/res/snmp?start=0&size=10000&desc=false&total=false"
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            snmp_templates = (json.loads(response.text))
            template = None
            if type(snmp_templates['snmpParamTemplate']) is dict:
                my_templates = [snmp_templates['snmpParamTemplate']]
                snmp_templates['snmpParamTemplate'] = my_templates
            if template_name is None:
                return snmp_templates['snmpParamTemplate']
            elif template_name is not None:
                for snmp_template in snmp_templates['snmpParamTemplate']:
                    if snmp_template['name'] == template_name:
                        template = [snmp_template]
                if template == None:
                    return 404
                else:
                    return template
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_snmp_templates: An Error has occured"


def modify_snmp_template(auth, url, snmp_template, template_name= None, template_id = None):
    """
    Function takes input of a dictionry containing the required key/value pair for the modification
    of a snmp template.

    :param auth:
    :param url:
    :param ssh_template: Human readable label which is the name of the specific ssh template
    :param template_id Internal IMC number which designates the specific ssh template
    :return: int value of HTTP response code 201 for proper creation or 404 for failed creation
    :rtype int

    Sample of proper KV pairs. Please see documentation for valid values for different fields.

    snmp_template =  {
      "version": "2",
      "name": "new_snmp_template",
      "type": "0",
      "paraType": "SNMPv2c",
      "roCommunity": "newpublic",
      "rwCommunity": "newprivate",
      "timeout": "4",
      "retries": "4",
      "contextName": "",
      "securityName": " ",
      "securityMode": "1",
      "authScheme": "0",
      "authPassword": "",
      "privScheme": "0",
      "privPassword": "",
      "snmpPort": "161",
      "isAutodiscoverTemp": "1",
      "creator": "admin",
      "accessType": "1",
      "operatorGroupStr": ""
      }
    """
    if template_name is None:
        template_name = snmp_template['name']
    if template_id is None:
        snmp_templates = get_snmp_templates(auth, url)
        template_id = None
        for template in snmp_templates:
            if template['name'] == template_name:
                template_id = template['id']
    f_url = url + "/imcrs/plat/res/snmp/"+str(template_id)+"/update"
    response = requests.put(f_url, data = json.dumps(snmp_template), auth=auth, headers=HEADERS)
    try:
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " modify_snmp_template: An Error has occured"


def delete_snmp_template(auth, url, template_name= None, template_id= None):
    """
    Takes template_name as input to issue RESTUL call to HP IMC which will delete the specific
    snmp template from the IMC system

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param template_name: str value of template name

    :param template_id: str value template template_id value

    :return: int HTTP response code

    :rtype  int
    """
    try:
        if template_id is None:
            snmp_templates = get_snmp_templates(auth, url)
            if template_name is None:
                template_name = snmp_template['name']
            template_id = None
            for template in snmp_templates:
                if template['name'] == template_name:
                    template_id = template['id']
        f_url = url + "/imcrs/plat/res/snmp/%s/delete" % template_id
        response = requests.delete(f_url, auth=auth, headers=HEADERS)
        return response.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " delete_snmp_template: An Error has occured"

