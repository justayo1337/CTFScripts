#! /usr/bin/env python3
import requests
import sys
host= sys.argv[1]
print ("\033[1;37;40mChecking " + host + "...")
def checkDomain(host):
	if "http://" not in host:
		host="http://" + host
	else:
		pass
	code = requests.get(host).status_code
	if code==404:
		pass
	else:	
		print("\033[1;32;40m" + host+ " is probably accessible with code - " + str(code))
		
checkDomain(host)
