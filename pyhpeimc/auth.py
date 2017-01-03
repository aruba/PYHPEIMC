#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for authenticating to the HPE IMC NMS platform
using the RESTful API

"""

# This section imports required libraries
import json

import requests

HEADERS = {'Accept': 'application/json', 'Content-Type':
           'application/json', 'Accept-encoding': 'application/json'}


class IMCAuth(requests.auth.HTTPDigestAuth):
    """
    This class handles authentication against the HPE IMC API and uses the Requests API. IMCAuth
    derives from requests.auth.HTTPDigestAuth.

    >>> auth = IMCAuth("http://", "10.101.0.204", "8080", "admin", "admin")

    >>> auth.password
    'admin'

    """

    def __init__(self, h_url, server, port, username, password):
        """
        Initializes the class. Set the h_url, server, username, and password variables.
        :param h_url: str value. Must be equal to "http://" or "https://
        :param server: str value. Must be valid IPv4 address or FQDN
        :param port: str value. Equal to listening port of IMC server. example "8080" for http
        or "8443" for HTTPS
        :param username: str value. Equal to username of IMC operator with privileges to access
        RESTUL API
        :param password: str value. Equal to valid password of username defined above
        :return:
        returns HTTPDigestauth object
        """
        super(IMCAuth, self).__init__(username, password)
        self.h_url = h_url
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.url = self.h_url + self.server + ":" + self.port
        self.creds = requests.auth.HTTPDigestAuth(self.username, self.password)

    def get_auth(self):
        """
        This method requests an authentication object from the HPE IMC NMS and returns an
        HTTPDigest Auth Object
        :return:
        """
        url = self.h_url + self.server + ":" + self.port
        auth = requests.auth.HTTPDigestAuth(self.username, self.password)
        f_url = url + "/imcrs"
        try:
            response = requests.get(f_url, auth=auth, headers=HEADERS, verify=False)
            if response.status_code != 200:  # checks for valid IMC credentials
                print("Error:\n" + "Error: \n You're credentials are invalid. Please try again\n\n")
                set_imc_creds()
            return response.status_code
        except requests.exceptions.RequestException as error:
            return "Error:\n" + str(error) + 'The IMC server address is invalid. Please try again'


def check_imc_creds(auth, url):
    """Function takes input of auth class object auth object and URL and returns a BOOL of TRUE
     if the authentication was successful.

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> check_imc_creds(auth.creds, auth.url)
    True

    """
    test_url = '/imcrs'
    f_url = url + test_url
    try:
        response = requests.get(f_url, auth=auth, headers=HEADERS, verify=False)
        return bool(response.status_code == 200)
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " test_imc_creds: An Error has occured"


def set_imc_creds(h_url=None, imc_server=None, imc_port=None, imc_user=None, imc_pw=None):
    """ This function prompts user for IMC server information and credentuials and stores
    values in url and auth global variables"""
    if h_url is None:
        imc_protocol = input("What protocol would you like to use to connect to the "
                             "IMC server: \n Press 1 for HTTP: \n Press 2 for HTTPS:")
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
        response = requests.get(f_url, auth=auth, headers=HEADERS, verify=False)
        print(response.status_code)
        if response.status_code != 200:  # checks for valid IMC credentials
            print("Error: \n You're credentials are invalid. Please try again\n\n")
            set_imc_creds()
        else:
            print("You've successfully access the IMC eAPI")
            return auth
    except requests.exceptions.RequestException as error:
        print("Error:\n" + str(error))
        print("\n\nThe IMC server address is invalid. Please try again\n\n")
        set_imc_creds()


# This section contains misc helper functions as needed.


def print_to_file(object_name):
    """
    Function takes in object of type str, list, or dict and prints out to current working
    directory as pyoutput.txt
    :param:  Object: object of type str, list, or dict
    :return: No return. Just prints out to file handler and save to current working directory as
    pyoutput.txt
    """
    with open('pyoutput.txt', 'w') as filehandler:
        output = None
        if isinstance(object_name, list):
            output = json.dumps(object, indent=4)
        if isinstance(object_name, dict):
            output = json.dumps(object, indent=4)
        if isinstance(object_name, str):
            output = object_name
        filehandler.write(output)
