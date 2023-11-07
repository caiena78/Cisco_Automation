# Cisco Automation examples
    I have created 3 different want to automate a Cisco Device
        1. Netmiko_CLI  - Automate the deivce with CLI commands 
        2. Restconf     - Automate the device with the rest api
        2. Netconf      - Automate the device with netconf  (The python driver ncclient  only works on linux and mac)

# Models
    Cisco Restconf and Netconf are based on models, I have included the model i work with in the Models folder

# Prerequisite
   Download and install python from https://www.python.org/downloads/ you will also need to add it to your path.
   Download git from https://git-scm.com/downloads

   Git clone this repository with.

      git clone https://github.com/caiena78/Cisco_Automation.git
   
   install the python requirements with

      run "pip install -r requirements.txt" 


# Running the Examples
     from the command prompt change into the directory you want to try.
     - Netmiko_CLI
        
        pip install -r requirement.txt
        
        python show_run.py --deviceip "192.168.x.x" --username <username>  --password <password>

     - Restconf_JSON
        
        pip install -r requirement.txt
        
        python Restconf_show_run.py --deviceip "192.168.x.x" --username <username>  --password <password>

     - Netconf_XML  <-- The python driver ncclient  only works on linux and mac
        
        pip install -r requirement.txt
        
        python Netconf_show_run.py --deviceip "192.168.x.x" --username <username>  --password <password>