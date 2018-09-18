# -*- coding: utf-8 -*-
""" This file is used to populate values to select what specific vendors to test various vendors
specific functionality again. If you do not have a specific vendors device, or don't wish to test against
a specific vendors device, change the value of that specific variable to None and all
tests associated with that specific vendor will automatically be skipped."""

from pyhpeimc.auth import *

auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")



# Tests will use the following IP addresses for specific tests


DoesntExist = '8.8.8.8' # Chose an IP address which you know doesn't exist in your IMC system
term_access_host = '10.101.0.51'

# Used for pyhpeimc.plat.termaccess to test IP address manager functions. Suggest using
# IP address range that does not exist on the managed network
term_access_ipam_network_scope = '10.50.0.0/16'  # Used for pyhpeimc_plat_termaccess IP Address Manager Functions
term_access_ipam_child_scope = '10.50.0.0/24'  # used for pyhpeimc_plat_termaccess IP address Manager functions
term_access_ipam_host = '10.50.0.5'  # Used for pyhpeimc_plat_termaccess IP Address Manager Functions

# used for testing VLAN functions to create and destroy vlans during tests
vlanid = '500'
vlan_name = 'Test_Vlan'

# Switches
CW3_Switch = None
CW3_Interface = None
CW5_Switch = '10.101.0.221'
CW5_Interface = '9'
CW7_Switch = None
Cisco_Switch = None
Juniper_Switch = None
Arista_Switch = None
ArubaOS_Switch = None

# Routers
Cisco_Router = None
CW5_Router = None
Juniper_Router = None

# Servers
Windows_Server = None
Linux_Server = None

# Wireless
CW5_Wireless = None
Aruba = None
MSM = None
CiscoWireless = None

# Hypervisor
ESX = None
HyperV = None

# Set to True if you wish to test the set_interface_up and set_interface_down functions in
# the test_pyhpeimc_plat_device test file. Warning - Setting these values to True may disrupt
# access to your network devices and require manual intervention to repair if connectivity to
# the IMC system is lost.
test_interface_up = False

test_interface_down = False

'''
#Template for building Multiple Vendor Tests

"""============================================================================================="""

#####Test TEST_NAME_HERE for Multiple Vendor Devices

###Switches

#CW3_Switch



#CW5_Switch
class Test_Function_Name_CW5_Switch(TestCase):
    def test_Function_Name_type(self):
        if CW5_Switch is None:
            raise SkipTest
        self.fail()
    def test_Function_Name_content(self):
        if CW5_Switch is None:
            raise SkipTest
            self.fail()


#CW7_Switch



#Cisco_Switch



#Juniper_Switch


#Arista_Switch




#ArubaOS_Switch (Formerly Provision)



###Routers

#Cisco_Router


#CW5_Router


#Juniper_Router (SRV)


#Wireless

#CW5_Wireless

#Aruba

#MSM

#CiscoWireless



####Servers


#Windows_Server



#Linux_Server


###Hypervisors


#ESX



#HyperV

#DoesntExist

'''
