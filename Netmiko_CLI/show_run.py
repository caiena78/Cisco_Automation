

# This Script sends a "show run" to a cisco IOS/IOSXE Device 
# 
# before you run this script install the requirments with the following commands
#  pip install requirments.txt 
#
# Run Example
# python show_run.py --deviceip "192.168.x.x" --username <username>  --password <password>



from netmiko import ConnectHandler 
import argparse


# Returns all parmaters for netmiko to login to the device
def ios(ip,user,password):    
    device={
        'device_type': 'cisco_ios',
        'host':   ip,
        'username': user,
        'password': password,
        'port' : 22,          # optional, defaults to 22   
        'conn_timeout' : 40,
        'global_delay_factor': 30,      
    }     
    return device

#sends commands to the device, example ("show run , show interface")
def sendCMD(device,command):
    with  ConnectHandler(**device) as net_connect:                
        Data = net_connect.send_command(command,use_textfsm=True)        
    return Data




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI show run')
    parser.add_argument('--deviceip', default='',help="Device ip")     
    parser.add_argument('--username',default='', help="username")
    parser.add_argument('--password',default='',help="Password")
    args = parser.parse_args()
    

    switch=ios(args.deviceip,args.username,args.password)
    cmd="show run"
    
    output=sendCMD(switch,cmd)
    print(output)
   


