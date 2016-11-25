from pyhpeimc.auth import *

auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

router = '10.101.0.1'

#Tests will use the following IP addresses for specific tests

#Switches
CW3_Switch = None
CW5_Switch = '10.101.0.221'
CW7_Switch = '10.20.10.10'
Cisco_Switch = None
Juniper_Switch = None
Arista_Switch = '10.101.0.249'
ArubaOS_Switch = None


#Routers
Cisco_Router = '10.101.0.1'
CW5_Router = None
Juniper_Router = None

#Servers
Windows_Server = '10.101.0.21'
Linux_Server = '10.101.0.51'
#Wireless
cw5 = '10.101.0.31'
#Hypervisor
ESX= '10.101.0.6'
HyperV = None



"""============================================================================================="""

#####Test TEST_NAME_HERE for Multiple Vendor Devices

###Switches

#CW3_Switch


#CW5_Switch


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


#VMWare ESX


#HyperV