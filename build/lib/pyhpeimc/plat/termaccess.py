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

# This section imports required libraries
import json
import requests
import ipaddress


HEADERS = {'Accept': 'application/json', 'Content-Type':
    'application/json', 'Accept-encoding': 'application/json'}





def get_real_time_locate(ipAddress, auth, url):
    """
    function takes the ipAddress of a specific host and issues a RESTFUL call to get the device and interface that the
    target host is currently connected to.
    :param ipAddress: str value valid IPv4 IP address
    :return: dictionary containing hostIp, devId, deviceIP, ifDesc, ifIndex
    """
    real_time_locate_url = "/imcrs/res/access/realtimeLocate?type=2&value=" + str(ipAddress) + "&total=false"
    f_url = url + real_time_locate_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            response =  json.loads(r.text)
            if 'realtimeLocation' in response:
                real_time_locate = json.loads(r.text)['realtimeLocation']
                if type(real_time_locate) is dict:
                    real_time_locate = [real_time_locate]
                    return real_time_locate
                else:
                    return json.loads(r.text)['realtimeLocation']
            else:
                return json.loads(r.text)

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_real_time_locate: An Error has occured"


def get_ip_mac_arp_list(devId, auth,url):
    """
    function takes devid of specific device and issues a RESTFUL call to get the IP/MAC/ARP list from the target device.
    :param devId: int or str value of the target device.
    :return: list of dictionaries containing the IP/MAC/ARP list of the target device.
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()
    ip_mac_arp_list_url = "/imcrs/res/access/ipMacArp/" + str(devId)
    f_url = url + ip_mac_arp_list_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            macarplist = (json.loads(r.text))
            if len(macarplist) > 1:
                return macarplist['ipMacArp']
            else:
                return ['this function is unsupported']

    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_mac_arp_list: An Error has occured"


#this section deals with the IP Address Manager functions with terminal access of HPE IMC Base platform

def get_ip_scope(auth, url,scopeId=None):
    """
    function requires no inputs and returns all IP address scopes currently configured on the HPE IMC server. If the
    optional scopeId parameter is included, this will automatically return only the desired scope id.
    :param scopeId: integer of the desired scope id ( optional )
    :param auth:
    :return:
    """
    if scopeId is None:
        get_ip_scope_url = "/imcrs/res/access/assignedIpScope"
    else:
        get_ip_scope_url = "/imcrs/res/access/assignedIpScope/ip?ipScopeId="+str(scopeId)

    f_url = url + get_ip_scope_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            ipscopelist = (json.loads(r.text))
            return ipscopelist['assignedIpScope']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_scope: An Error has occured"

def get_ip_scope_detail(auth, url,scopeId=None):
    """
    function requires no inputs and returns all IP address scopes currently configured on the HPE IMC server. If the
    optional scopeId parameter is included, this will automatically return only the desired scope id.
    :param scopeId: integer of the desired scope id ( optional )
    :param auth:
    :return:
    """
    get_ip_scope_url = "/imcrs/res/access/assignedIpScope/"+str(scopeId)

    f_url = url + get_ip_scope_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            ipscopelist = (json.loads(r.text))
            return ipscopelist
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_scope: An Error has occured"


def get_ip_scope_hosts(auth, url, scopeId):
    """
    Function requires input of scope ID and returns list of allocated IP address for the specified scope
    :param auth:
    :param url:
    :param scopeId: Interger of teh desired scope id
    :return:
    """
    get_ip_scope_url = "/imcrs/res/access/assignedIpScope/ip?size=10000&ipScopeId="+str(scopeId)
    f_url = url + get_ip_scope_url
    r = requests.get(f_url, auth=auth, headers=HEADERS)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            ipscopelist = (json.loads(r.text))
            return ipscopelist['assignedIpInfo']
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " get_ip_scope: An Error has occured"






def add_ip_scope(auth, url,startIp, endIp, name, description):
    """
    Function takes input of four strings Start Ip, endIp, name, and description to add new Ip Scope to terminal access
    in the HPE IMC base platform
    :param startIp: str Start of IP address scope ex. '10.101.0.1'
    :param endIp: str End of IP address scope ex. '10.101.0.254'
    :param name: str Name of the owner of this IP scope  ex. 'admin'
    :param description: str description of the Ip scope
    :return:
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()

    add_ip_scope_url = "/imcrs/res/access/assignedIpScope"
    f_url = url + add_ip_scope_url
    payload = ('''{  "startIp": "%s", "endIp": "%s","name": "%s","description": "%s" }'''
               %(str(startIp), str(endIp), str(name), str(description)))
    r = requests.post(f_url, auth=auth, headers=HEADERS, data=payload) # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print ("IP Scope Already Exists")
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"

def add_child_ip_scope(auth, url,startIp, endIp, name, description, scopeid):
    """
    Function takes input of four strings Start Ip, endIp, name, and description to add new Ip Scope to terminal access
    in the HPE IMC base platform
    :param startIp: str Start of IP address scope ex. '10.101.0.1'
    :param endIp: str End of IP address scope ex. '10.101.0.254'
    :param name: str Name of the owner of this IP scope  ex. 'admin'
    :param description: str description of the Ip scope
    :return:
    """
    if auth is None or url is None:  # checks to see if the imc credentials are already available
        set_imc_creds()

    add_ip_scope_url = "/imcrs/res/access/assignedIpScope/" + str(scopeid)
    f_url = url + add_ip_scope_url
    payload = ('''{  "startIp": "%s", "endIp": "%s","name": "%s","description": "%s", "parentId" : "%s"}'''
               %(str(startIp), str(endIp), str(name), str(description), str(scopeid)))
    r = requests.post(f_url, auth=auth, headers=HEADERS, data=payload) # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print ("Conflict with Current Scope")
            return r.status_code
    except requests.exceptions.RequestException as e:
            return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"

def add_scope_ip(ipaddress, name, description, scopeid, auth, url):
    """
    Function to add new IP address allocation to existing scope ID
    :param ipaddress:
    :param name:
    :param description:
    :param auth:
    :param url:
    :return:
    """
    new_ip = { "ip": ipaddress,
      "name": name,
      "description": description}
    add_scope_ip_url = '/imcrs/res/access/assignedIpScope/ip?ipScopeId='+str(scopeid)
    f_url = url + add_scope_ip_url
    payload = json.dumps(new_ip)
    r = requests.post(f_url, auth=auth, headers=HEADERS,
                      data=payload)  # creates the URL using the payload variable as the contents
    try:
        if r.status_code == 200:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print("IP Scope Already Exists")
            return r.status_code
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"

def remove_scope_ip(hostid, auth, url):
    """
    Function to add new IP address allocation to existing scope ID
    :param ipaddress:
    :param name:
    :param description:
    :param auth:
    :param url:
    :return:
    """
    add_scope_ip_url = '/imcrs/res/access/assignedIpScope/ip/'+str(hostid)
    f_url = url + add_scope_ip_url

    r = requests.delete(f_url, auth=auth, headers=HEADERS,
                      )
    try:
        if r.status_code == 200:
            print("IP Scope Successfully Created")
            return r.status_code
        elif r.status_code == 409:
            print("IP Scope Already Exists")
            return r.status_code
    except requests.exceptions.RequestException as e:
        return "Error:\n" + str(e) + " add_ip_scope: An Error has occured"



def get_scope_id(network_address, auth, url):
    netaddr = ipaddress.ip_network(network_address)
    scopes = get_ip_scope(auth, url)
    for i in scopes:
        if int(i['id']) > 0:
            if ipaddress.ip_address(i['startIp']) in netaddr and ipaddress.ip_address(i['endIp']) in netaddr:
                return i['id']
            if "assignedIpScope" in i:
                for child in i['assignedIpScope']:
                    if ipaddress.ip_address(child['startIp']) in netaddr and ipaddress.ip_address(child['endIp']) in netaddr:

                        return child['id']









    #Add host to IP scope
    #http://10.101.0.203:8080/imcrs/res/access/assignedIpScope/ip?ipScopeId=1
    '''{
      "ip": "10.101.0.1",
      "name": "Cisco2811.lab.local",
      "description": "Cisco 2811",
      "parentId": "18"
    }'''