#this script get some basic information on one device via mac address.
# python get-wireless-client.py --deviceip <ip> --username <username> --password <password> --mac 00:00:de:ad:be:ef


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
    required = parser.add_argument_group('required arguments')
    parser.add_argument('--deviceip', default='',help="Device ip")     
    parser.add_argument('--username',default='', help="username")
    parser.add_argument('--password',default='',help="Password")
    parser.add_argument('--mac', default="00:00:de:ad:be:ef")
    
    args = parser.parse_args()
    

    device = {"ip": args.deviceip, "port": "443", "user": args.username, "password": args.password, "mac": args.mac}
   

    url = f"https://{device['ip']}:{device['port']}/restconf/data/Cisco-IOS-XE-wireless-client-oper:client-oper-data/dot11-oper-data={device['mac']}"

 

    #get the data from the device
    data=getdata(device,url)
  
    # write the data to a file
    filename=args.deviceip.replace(".","_")+".json"
    
    jdata=json.dumps(data,indent=4)
    with open(filename,'w') as w:
        w.write(jdata)




