#!/usr/bin/env python

import os
import sys

def configureInterfaces():
    interfaceFile = sys.argv[1]
    staticIp = sys.argv[2]
    netmask = sys.argv[3]
    gateway = sys.argv[4]
    dns = sys.argv[5]

    f = open(interfaceFile, 'w+')
    f.write("auto " + interfaceFile + "\n"
            + "iface " + interfaceFile + " inet static\n"
            + "address " + staticIp + "\n"
            + "netmask " + netmask + "\n"
            + "gateway " + gateway + "\n"
            + "dns-nameservers " + dns)
    f.close()

def checkPermission():
    if os.geteuid() is 0:
        configureInterfaces()
    else:
        print("User must be root")

if __name__ == "__main__":
    checkPermission()

