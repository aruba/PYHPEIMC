__author__ = 'christopheryoung'

from pyhpeimc import *

switchlist = ['10.101.0.221'],  '10.101.0.233','10.254.0.101']
switch_count = 1
routerlist = ['10.101.0.1']
router_count = 1
hypervisorlist = ['10.101.0.3', '10.101.0.4', '10.101.0.6', '10.101.0.7']
hypervisor_count = 1
hostlist = ['10.101.16.100','10.101.16.101']
host_count = 1
aclist = ['10.101.0.235', '10.101.0.230']
ac_count = 1
serverlist = []
server_count = 1
storagelist = []
storage_count = 1


def create_switch(devname, ipaddress):
    devname = IMCDev(ipaddress)
    return devname


def testswitch(switchlist):
    global switch_count
    switches = []
    for i in switchlist:
        devname = 'dev'+str(count)
        switch = create_switch(devname, i)
        switches.append(switch)
        switch_count = switch_count +1
    return switches

switches = testswitch(switchlist)




