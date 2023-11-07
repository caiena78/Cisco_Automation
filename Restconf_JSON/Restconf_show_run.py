# This Script sends a Get config (show run) to a cisco Device with Restconf enabled
# 
#
# before you run this script install the requirments with the following commands
#  pip install -r requirments.txt 
#
# Run Example
# python Restconf_show_run.py --deviceip "192.168.x.x" --username <username>  --password <password>


import requests
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
# this stops the warning with the untrusted cerfitcate
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
import argparse



def getdata(device,url):
    headers = {"Accept": "application/yang-data+json", "Content-Type": "application/yang-data+json"}
    response = requests.get(url, headers=headers, auth=(device['user'], device['password']), verify=False)
    return response.json()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI show run')
    parser.add_argument('--deviceip', default='',help="Device ip")     
    parser.add_argument('--username',default='', help="username")
    parser.add_argument('--password',default='',help="Password")
    args = parser.parse_args()
    
    # set up connection parameters in a dictionary
    device = {"ip": args.deviceip, "port": "443", "user": args.username, "password": args.password}
    
    #Set the url for Restconf on the device
    url = f"https://{device['ip']}:{device['port']}/restconf/data/Cisco-IOS-XE-native:native"

    #get the data from the device
    data=getdata(device,url)
  
    # write the data to a file
    filename=args.deviceip.replace(".","_")+".json"
    
    jdata=json.dumps(data,indent=4)
    with open(filename,'w') as w:
        w.write(jdata)

    
    
  
            