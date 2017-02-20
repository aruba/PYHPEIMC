#!/usr/bin/env python3
# author: @netmanchris

# This section imports required libraries
import requests
import json



HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}


"""
This section deals with HPE IMC Operator Functions
"""

def create_operator(operator, auth, url,headers=HEADERS):
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

    >>>  operator = '''{ "fullName" : "test administrator"   ,
             "sessionTimeout" : "30",
             "password" :  "password",
             "operatorGroupId" : "1",
             "name" : "testadmin",
             "desc" : "test admin account",
             "defaultAcl" : "",
             "authType"  : "0"}'''

    >>> operator = json.loads(operator)

    >>> create_operator(operator, auth.creds, auth.url)
    Operator Successfully Created

    """
    create_operator_url = '/imcrs/plat/operator'
    f_url = url + create_operator_url
    print (f_url)
    payload = json.dumps(operator, indent=4)
    # creates the URL using the payload variable as the contents
    r = requests.post(f_url, data=payload, auth=auth, headers=headers)
    try:
        if r.status_code == 409:
            print("Operator Already Exists")
            return r.status_code
        elif r.status_code == 201:
            print("Operator Successfully Created")
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + ' create_operator: An Error has occured'

def set_operator_password(operator, password, auth, url,headers=HEADERS):
    """
    Function to set the password of an existing operator

    :param operator: str Name of the operator account

    :param password: str New password

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param headers: json formated string. default values set in module

    :return: int of 204 if successfull,

    :rtype: int

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.operator import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> set_operator_password('testadmin', 'newpassword', auth.creds, auth.url)
    Operator:testadmin password was successfully changed
    204

       """
    if operator == None:
        operator = input(
            '''\n What is the username you wish to change the password?''')
    oper_id = ''
    plat_oper_list = get_plat_operator(auth, url)
    for i in plat_oper_list:
        if i['name'] == operator:
            oper_id = i['id']
            authType = i['authType']
    if oper_id == '':
        return("\n User does not exist")
    change_pw_url = "/imcrs/plat/operator/"
    f_url = url + change_pw_url + oper_id
    if password is None:
        password = input(
        '''\n ============ Please input the operators new password:\n ============  ''')
    payload = json.dumps({'password': password , 'authType': authType})
    r = requests.put(f_url, data=payload, auth=auth, headers=headers)
    try:
        if r.status_code == 204:
            print("\n Operator:" + operator +
                  " password was successfully changed")
            return r.status_code
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + ' set_operator_password: An Error has occured'

def get_plat_operator(auth, url,headers=HEADERS):
    '''
    Funtion takes no inputs and returns a list of dictionaties of all of the operators currently configured on the HPE
    IMC system

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element represents one operator

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.operator import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> get_plat_operator(auth.creds, auth.url)

    '''
    get_operator_url = '/imcrs/plat/operator?start=0&size=1000&orderBy=id&desc=false&total=false'
    f_url = url + get_operator_url
    try:
        r = requests.get(f_url, auth=auth, headers=headers)
        plat_oper_list = json.loads(r.text)['operator']
        if type(plat_oper_list) is dict:
            oper_list = []
            oper_list.append(plat_oper_list)
            return oper_list
        return plat_oper_list
    except requests.exceptions.RequestException as e:
        print ("Error:\n" + str(e) + ' get_plat_operator: An Error has occured')
        return "Error:\n" + str(e) + ' get_plat_operator: An Error has occured'

def delete_plat_operator(operator,auth, url, headers=HEADERS):
    """
    Function to set the password of an existing operator
    :param operator: str Name of the operator account

    :param auth: requests auth object #usually auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usually auth.url from pyhpeimc.auth.authclass

    :param headers: json formated string. default values set in module

    :return: int of 204 if successfull

    :rtype: int

    >>> delete_plat_operator('testadmin', auth.creds, auth.url)
    Operator: testadmin was successfully deleted
    204
    """
    #oper_id = None
    plat_oper_list = get_plat_operator(auth, url)
    for i in plat_oper_list:
        if operator == i['name']:
            oper_id = i['id']
    if oper_id == None:
        return("\n User does not exist")
    delete_plat_operator_url = "/imcrs/plat/operator/"
    f_url = url + delete_plat_operator_url + str(oper_id)
    r = requests.delete(f_url, auth=auth, headers=headers)
    try:
        if r.status_code == 204:
            print("\n Operator: " + operator +
                  " was successfully deleted")
            return r.status_code
    except requests.exceptions.RequestException as e:
        print ("Error:\n" + str(e) + ' delete_plat_operator: An Error has occured')
        return "Error:\n" + str(e) + ' delete_plat_operator: An Error has occured'


