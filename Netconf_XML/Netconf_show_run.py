# This Script sends a Get config (show run) to a cisco Device with Netconf enabled
# 
#   *********ncclient only works on Linux and Mac***********
#
# before you run this script install the requirments with the following commands
#  pip install -r requirments.txt 
#
# Run Example
# python Netconf_show_run.py --deviceip "192.168.x.x" --username <username>  --password <password>



import sys
from argparse import ArgumentParser
from ncclient import manager
import json

import xml.dom.minidom


if __name__ == '__main__':
    parser = ArgumentParser(description='Select options.')
    # Input parameters
    parser.add_argument('--host', type=str, required=True,
                        help='The device IP or DN. Required')
    parser.add_argument('-u', '--username', type=str, required=True,
                        help='Username on the device. Required')
    parser.add_argument('-p', '--password', type=str, required=True,
                        help='Password for the username. Required')
    parser.add_argument('--port', type=int, default=830,
                        help='Specify this if you want a non-default port. Default: 830')

    args = parser.parse_args()

    m = manager.connect(host=args.host,
                        port=args.port,
                        username=args.username,
                        password=args.password,
                        device_params={'name':'iosxe'})

    reply =  m.get_config(source='running').data_xml  


    # Pretty print the XML reply
    xmlDom = xml.dom.minidom.parseString(str(reply))
    print(xmlDom.toprettyxml(indent='  '))

    #write the output to a file named switch.xml
    with open("switch.xml","w") as f:
        f.write(xmlDom.toprettyxml(indent='  '))