'''Copyright 2015 Chris Young

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''

#   IMC Server Build Project 1.0
#  Chris Young a.k.a Darth
#
# Hewlett Packard Company    Revision 1.0
#
# Change History.... 3/19/15
#

# This series of functions is intended to help automate the build of an IMC server using
# the eAPI function. The eAPI is available natively on the IMC enterprise edition
# and can be added to the standard edition through the purchase of the
# eAPI addon license.

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
    :param url: str url of IMC server, see requests library docs for more info
    :param auth: str see requests library docs for more info
    :param operator: dictionary with the required operator key-value pairs as defined above.
    :param headers: json formated string. default values set in module
    :return:
    """
    # checks to see if the imc credentials are already available
    if auth == None or url == None:
        imc_creds()
    create_operator_url = '/imcrs/plat/operator'
    f_url = url + create_operator_url
    # opens imc_operator_list.csv file
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
    :param url: str url of IMC server, see requests library docs for more info
    :param auth: str see requests library docs for more info
    :param headers: json formated string. default values set in module
    :return:
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
    :return: list of dictionaries
    '''
    get_operator_url = '/imcrs/plat/operator?start=0&size=1000&orderBy=id&desc=false&total=false'
    f_url = url + get_operator_url
    try:
        r = requests.get(f_url, auth=auth, headers=headers)
        plat_oper_list = json.loads(r.text)
        if type(plat_oper_list) is dict:
            oper_list = [plat_oper_list['operator']]
            #plat_oper_list[0] = plat_oper_list['operator']
            return oper_list
        return plat_oper_list['operator']
    except requests.exceptions.RequestException as e:
        print ("Error:\n" + str(e) + ' get_plat_operator: An Error has occured')
        return "Error:\n" + str(e) + ' get_plat_operator: An Error has occured'

def delete_plat_operator(operator,auth, url, headers=HEADERS):
    """
    Function to set the password of an existing operator
    :param operator: str Name of the operator account
    :param password: str New password
    :param url: str url of IMC server, see requests library docs for more info
    :param auth: str see requests library docs for more info
    :param headers: json formated string. default values set in module
    :return:
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


