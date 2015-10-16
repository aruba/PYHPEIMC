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
#Hewlett Packard Company    Revision 1.0
#
#Change History.... 3/19/15
#

#This series of functions is intended to help automate the build of an IMC server using
#the eAPI function. The eAPI is available natively on the IMC enterprise edition
#and can be added to the standard edition through the purchase of the eAPI addon license.

#This section imports required libraries
import requests, json, sys, time, subprocess, csv, os, ipaddress, pyhpimc
from requests.auth import HTTPDigestAuth


#url header to preprend on all IMC eAPI calls
url = None

#auth handler for eAPI calls
auth = None

#headers forcing IMC to respond with JSON content. XML content return is the default
headers = {'Accept': 'application/json', 'Content-Type': 'application/json','Accept-encoding': 'application/json'}


def real_time_locate(ipAddress):
    if auth == None or url == None:  # checks to see if the imc credentials are already available
        imc_creds()
    real_time_locate_url = "/imcrs/res/access/realtimeLocate?type=2&value="+ipAddress+"&total=false"
    f_url = url + real_time_locate_url
    r = requests.get(f_url, auth=auth, headers=headers)   #creates the URL using the payload variable as the contents
    if r.status_code == 200:
        return (json.loads(r.text)['realtimeLocation'])
          
    else:
     print (r.status_code)
     print ("An Error has occured")
                         
        
        






#This sections contains helper functions leveraged by other other functions

def imc_creds():
    ''' This function prompts user for IMC server information and credentuials and stores
    values in url and auth global variables'''
    global url, auth, r
    imc_protocol = input("What protocol would you like to use to connect to the IMC server: \n Press 1 for HTTP: \n Press 2 for HTTPS:")
    if imc_protocol == "1":
        h_url = 'http://'
    else:
        h_url = 'https://'
    imc_server = input("What is the ip address of the IMC server?")
    imc_port = input("What is the port number of the IMC server?")
    imc_user = input("What is the username of the IMC eAPI user?")
    imc_pw = input('''What is the password of the IMC eAPI user?''')
    url = h_url+imc_server+":"+imc_port
    auth = requests.auth.HTTPDigestAuth(imc_user,imc_pw)
    test_url = '/imcrs'
    f_url = url+test_url
    try:
        r = requests.get(f_url, auth=auth, headers=headers)
    except requests.exceptions.RequestException as e:     #checks for reqeusts exceptions
            print ("Error:\n"+str(e))
            print ("\n\nThe IMC server address is invalid. Please try again\n\n")
            imc_creds()
    if r.status_code != 200:      #checks for valid IMC credentials
        print ("Error: \n You're credentials are invalid. Please try again\n\n")
        imc_creds()
    else:
        print ("You've successfully access the IMC eAPI")
    
    
#Defines the program to be run
        
def main():            
    add_device = input("Do you wish to change device categories now? Y/N:")
    if add_device.lower() == "y":
        change_dev_category()

    
    


if __name__ == "__main__":
    main()

