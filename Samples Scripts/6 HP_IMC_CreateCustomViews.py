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


#  IMC Server Build Project 1.0
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
import ipaddress
from requests.auth import HTTPDigestAuth


# url header to preprend on all IMC eAPI calls
url = None

# auth handler for eAPI calls
auth = None

# headers forcing IMC to respond with JSON content. XML content return is
# the default
headers = {'Accept': 'application/json', 'Content-Type':
           'application/json', 'Accept-encoding': 'application/json'}


def add_device_to_view(dev_list, view_id):
    modify_custom_view_url = '''/imcrs/plat/res/view/custom/''' + str(view_id)
    device_list = []
    for i in dev_list:
        dev_id = {'id': i['id']}
        device_list.append(dev_id)
    payload = '''{"device":''' + json.dumps(device_list) + '''}'''
    f_url = url + modify_custom_view_url
    # creates the URL using the payload variable as the contents
    r = requests.put(f_url, data=payload, auth=auth, headers=headers)
    r.status_code
    if r.status_code == 204:
        print("Device Succesfully Added")
    else:
        print("An Error has occured")


def create_new_view():
    view_name = input("Please input the name of the new view: ")
    add_view_url = "/imcrs/plat/res/view/custom?resPrivilegeFilter=false&desc=false&total=false"
    f_url = url + add_view_url
    payload = '''{ "name": "''' + view_name + '''", "autoAddDevType" : "0"}'''
    r = requests.post(f_url, data=payload, auth=auth,
                      headers=headers)  # creates the URL using the payload variable as the contents
    r.status_code
    if r.status_code == 201:
        return view_name
    else:
        print("An Error has occured")


def get_view_id(view_name):
    view_list = get_custom_views()
    for i in view_list:
        if i['name'].lower() == view_name.lower():
            view_id = i['symbolId']
            return i['symbolId']


def filter_dev_category():
    # checks to see if the imc credentials are already available
    if auth == None or url == None:
        imc_creds()
    global r
    category = None
    ip_range = None
    get_dev_list_url = None
    filter_by_cat = input("Do you want to filter by device category?\nY/N: ")
    if filter_by_cat.lower() == "y":
        print_dev_category()
        category = input("Please select the device category: ")
        get_dev_list_url = ("/imcrs/plat/res/device?resPrivilegeFilter=false&category=" +
                            category + "&start=0&size=10000&orderBy=id&desc=false&total=false")
        # return get_dev_list_url
    filter_by_ip = input(
        "Do you want to filter by IP address network range?\nY/N: ")
    if filter_by_ip.lower() == "y":
        ip_range = input(
            "What is the ip network range?\n Example: 10.101.16.\nFuzzy search is acceptible: ")
        if category == None:
            get_dev_list_url = ("/imcrs/plat/res/device?resPrivilegeFilter=false&ip=" +
                                ip_range + "&start=0&size=5&orderBy=id&desc=false&total=false")
        else:
            get_dev_list_url = ("/imcrs/plat/res/device?resPrivilegeFilter=false&category=" +
                                category + "&ip=" + ip_range + "&start=0&size=10000&orderBy=id&desc=false&total=false")
    f_url = url + get_dev_list_url

    payload = None
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    r.status_code
    if r.status_code == 200:
        dev_list = (json.loads(r.text))["device"]
        return dev_list
    else:
        print("An Error has occured")


def get_custom_views():
    # checks to see if the imc credentials are already available
    if auth == None or url == None:
        imc_creds()
    get_custom_view_url = '/imcrs/plat/res/view/custom?resPrivilegeFilter=false&desc=false&total=false'
    f_url = url + get_custom_view_url
    # creates the URL using the payload variable as the contents
    r = requests.get(f_url, auth=auth, headers=headers)
    if r.status_code == 200:
        view_list = (json.loads(r.text))["customView"]
        return view_list
    else:
        print("An Error has occured")


def find_a_view():
    view_name = input(
        "Please input the name of the view you wish to add devices to: ")
    view_list = get_custom_views()
    for i in view_list:
        if i['name'].lower() == view_name.lower():
            return i['symbolId']


# This sections contains helper functions leveraged by other other functions

def print_dev_category():
    categories = [{"categoryId": "0", "dev_type": "router"},
                  {"categoryId": "1", "dev_type": "switch"},
                  {"categoryId": "2", "dev_type": "server"},
                  {"categoryId": "3", "dev_type": "security"},
                  {"categoryId": "4", "dev_type": 'storage'},
                  {"categoryId": "5", "dev_type": "wireless"},
                  {"categoryId": "6", "dev_type": "voice"},
                  {"categoryId": "7", "dev_type": 'printer'},
                  {"categoryId": "8", "dev_type": 'ups'},
                  {"categoryId": "9", "dev_type": "desktop"},
                  {"categoryId": "10", "dev_type": "other"},
                  {"categoryId": "11", "dev_type": "surveillance"},
                  {"categoryId": "12", "dev_type": "video"},
                  {"categoryId": "13", "dev_type": "module"},
                  {"categoryId": "14", "dev_type": "virtualdev"},
                  {"categoryId": "15", "dev_type": "Load Balancer"},
                  {"categoryId": "16", "dev_type": "sdn_ctrl"}
                  ]
    for i in categories:
        print("For " + i["dev_type"] + ", Please press: " + i["categoryId"])


def imc_creds():
    ''' This function prompts user for IMC server information and credentuials and stores
    values in url and auth global variables'''
    global url, auth, r
    imc_protocol = input(
        "What protocol would you like to use to connect to the IMC server: \n Press 1 for HTTP: \n Press 2 for HTTPS:")
    if imc_protocol == "1":
        h_url = 'http://'
    else:
        h_url = 'https://'
    imc_server = input("What is the ip address of the IMC server?")
    imc_port = input("What is the port number of the IMC server?")
    imc_user = input("What is the username of the IMC eAPI user?")
    imc_pw = input('''What is the password of the IMC eAPI user?''')
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
        print("Error: \n You're credentials are invalid. Please try again\n\n")
        imc_creds()
    else:
        print("You've successfully access the IMC eAPI")


# Defines the program to be run

def main():
    # checks to see if the imc credentials are already available
    if auth == None or url == None:
        imc_creds()
    view_name = create_new_view()
    view_list = get_custom_views()
    view_id = get_view_id(view_name)
    dev_list = filter_dev_category()
    add_device_to_view(dev_list, view_id)


if __name__ == "__main__":
    main()
