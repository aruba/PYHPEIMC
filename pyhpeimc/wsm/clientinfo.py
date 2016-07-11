#!/usr/bin/env python3
# author: @netmanchris



# This section imports required libraries
import json
import requests



HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}

def get_client_info_all(auth, url):
    """
    function takes no input to RESTFUL call to HP IMC
    :return:list of dictionatires contraining the Wireless Client information as known by HPE IMC Wireless Services
    Manager module.
    """
    get_client_info_all_url = "/imcrs/wlan/clientInfo/queryAllClientBasicInfo"
    f_url = url + get_client_info_all_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['clientBasicInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_client_info_all: An Error has occured"


def get_client_online_history_all(auth, url):
    """
    function takes no input to RESTFUL call to HP IMC
    :return:list of dictionatires contraining the Wireless Client information as known by HPE IMC Wireless Services
    Manager module.
    """
    get_client_online_history_all_url = "/imcrs/wlan/clientInfo/queryClientOnlineHistoryInfo"
    f_url = url + get_client_online_history_all_url
    payload = None
    r = requests.get(f_url, auth=auth,
                     headers=HEADERS)  # creates the URL using the payload variable as the contents
    # print(r.status_code)
    try:
        if r.status_code == 200:
            if len(r.text) > 0:
                return json.loads(r.text)['clientOnlineHistoryInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_client_online_history_all: An Error has occured"