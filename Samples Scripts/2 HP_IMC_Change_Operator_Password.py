#!/usr/bin/env python3
# author: @netmanchris

""" Copyright 2015 Hewlett Packard Enterprise Development LP

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   """

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
import sys
import time
import subprocess
import csv
import os
from requests.auth import HTTPDigestAuth


# url header to preprend on all IMC eAPI calls
url = None

# auth handler for eAPI calls
auth = None

# headers forcing IMC to respond with JSON content. XML content return is
# the default
headers = {'Accept': 'application/json', 'Content-Type':
           'application/json', 'Accept-encoding': 'application/json'}


def create_operator():
    # checks to see if the imc credentials are already available
    if auth == None or url == None:
        imc_creds()
    create_operator_url = '/imcrs/plat/operator'
    f_url = url + create_operator_url
    # opens imc_operator_list.csv file
    with open('imc_operator_list.csv') as csvfile:
        # decodes file as csv as a python dictionary
        reader = csv.DictReader(csvfile)
        for operator in reader:
            # loads each row of the CSV as a JSON string
            payload = json.dumps(operator, indent=4)
            # creates the URL using the payload variable as the contents
            r = requests.post(f_url, data=payload, auth=auth, headers=headers)
            if r.status_code == 409:
                print("\n Operator Already Exists")
            elif r.status_code == 201:
                print("\n Operator Successfully Created")


def change_operator_pw(oper_name=None):
    if oper_name == None:
        oper_name = input(
            '''\n What is the username you wish to change the password?''')
    oper_id = ''
    get_plat_operator()
    for i in plat_oper_list['operator']:
        if i['name'] == oper_name:
            oper_id = i['id']
            authType = i['authType']
    if oper_id == '':
        print("\n User does not exist")
        run_again()
    change_pw_url = "/imcrs/plat/operator/"
    f_url = url + change_pw_url + oper_id
    payload = json.dumps({'password': input(
        '''\n ============ Please input the operators new password:\n ============  '''), 'authType': authType})
    r = requests.put(f_url, data=payload, auth=auth, headers=headers)
    if r.status_code == 204:
        print("\n Operator:" + oper_name +
              " password was successfully changed")
        run_again()

    else:
        print("\n Unknown Error")
        time.sleep(5)


# This sections contains helper functions leveraged by other other functions

def run_again():
    change_other = input(
        "\n Do you wish to change another HP IMC Operators Password? Y/N:")
    if change_other == "Y" or change_other == "y":
        change_operator_pw()
    else:
        sys.exit()


def get_plat_operator():
    global plat_oper_list
    # checks to see if the imc credentials are already available
    if auth == None or url == None:
        imc_creds()
    get_operator_url = '/imcrs/plat/operator?start=0&size=1000&orderBy=id&desc=false&total=false'
    f_url = url + get_operator_url
    r = requests.get(f_url, auth=auth, headers=headers)
    plat_oper_list = json.loads(r.text)
    return plat_oper_list


def imc_creds():
    ''' This function prompts user for IMC server information and credentuials and stores
    values in url and auth global variables'''
    global url, auth, r
    imc_protocol = input(
        "\n What protocol would you like to use to connect to the IMC server: \n Press 1 for HTTP: \n Press 2 for HTTPS:")
    if imc_protocol == "1":
        h_url = 'http://'
    else:
        h_url = 'https://'
    imc_server = input("\n What is the ip address of the IMC server?")
    imc_port = input("\n What is the port number of the IMC server?")
    imc_user = input("\n What is the username of the IMC eAPI user?")
    imc_pw = input('''\n What is the password of the IMC eAPI user?''')
    url = h_url + imc_server + ":" + imc_port
    auth = requests.auth.HTTPDigestAuth(imc_user, imc_pw)
    test_url = '/imcrs'
    f_url = url + test_url
    try:
        r = requests.get(f_url, auth=auth, headers=headers)
    # checks for reqeusts exceptions
    except requests.exceptions.RequestException as e:
        print("Error:\n" + str(e))
        print("\n\nThe IMC server address is invalid. Please try again\n\n")
        imc_creds()
    if r.status_code != 200:  # checks for valid IMC credentials
        print(
            "\n ============ \nError: \n You're credentials are invalid. Please try again: \n ============\n\n")
        imc_creds()
    else:
        print(
            "\n ============ \n You've successfully accessed the IMC eAPI \n ============")
        time.sleep(2)
        os.system('cls')


# Defines the program to be run

def main():
    print(
        '''\n\n==============\n\nThis tool is intended to help you change the password of an HP IMC platform\nOperator. \n\nThis tool is intended as a proof-of-concept and is provided as-is\nwith no warranty, expressed or implied\n\nThis tool is for HP internal use only and should be considered restricted\nand confidential.\n\n==============''')
    change_password = input(
        "Do you wish to change an HP IMC Operator Password? Y/N:")
    if change_password == "Y" or change_password == "y":
        change_operator_pw()


if __name__ == "__main__":
    main()
