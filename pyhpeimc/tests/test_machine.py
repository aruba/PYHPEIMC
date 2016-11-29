from pyhpeimc.auth import *

''' This file is used to populate values to select what specific vendors to test various vendors
specific functionality again. If you do not have a specific vendors device, or don't wish to test against
a specific vendors device, change the value of that specific variable to None and all
tests associated with that specific vendor will automatically be skipped.'''


auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")


#Tests will use the following IP addresses for specific tests

DoesntExist = '8.8.8.8' #Chose an IP address which you know doesn't exist in your IMC system
term_access_host = '10.101.0.51'

term_access_ipam_network_scope = '10.50.0.0/24' #Used for pyhpeimc_plat_termaccess IP Address Manager Functions
term_access_ipam_host = '10.50.0.5/24' #Used for pyhpeimc_plat_termaccess IP Address Manager Functions

#Switches
CW3_Switch = None
CW5_Switch = '10.101.0.221'
CW7_Switch = None
Cisco_Switch = None
Juniper_Switch = None
Arista_Switch = None
ArubaOS_Switch = None


#Routers
Cisco_Router = None
CW5_Router = None
Juniper_Router = None

#Servers
Windows_Server = None
Linux_Server = None
#Wireless
cw5 = None
#Hypervisor
ESX= None
HyperV = None


#Set to True if you wish to test the set_interface_up and set_interface_down functions in the test_pyhpeimc_plat_device test file.
#Warning - Setting these values to True may disrupt access to your network devices and require manual intervention to repair if
#connectivity to the IMC system is lost.
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



####Servers


#Windows_Server



#Linux_Server


###Hypervisors


#ESX



#HyperV

#DoesntExist

'''

