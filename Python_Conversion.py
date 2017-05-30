# Import Dependencies
import requests
import getpass
from base64 import b64encode
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

### Clear Screen
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "-cls" if system_name().lower()=="windows" else "clear"

    # Action
    system_call(command)


# Set Credentials
username = "admin" # Change this for your environment - we'll prompt for this later.
password = b64encode(username + ":" + getpass.getpass("Please enter your password for user " + username + ":"))
verify_SSL = False

prism_ip = "192.168.7.51"
service_url_v1 = "https://%s:9440/PrismGateway/services/rest/v1" % prism_ip
service_url_v2 = "https://%s:9440/api/nutanix/v2.0" % prism_ip



# Set API URLs
vm_api = service_url_v2 + "/vms/"
image_api = service_url_v2 + "/images/"
network_api = service_url_v2 + "/networks/"
cluster_api = service_url_v2 + "/cluster/"
container_api = service_url_v2 + "/storage_containers/"

# Set Request Headers - still necessary?
headers = {"Authorization" : "Basic %s" % password, "Content-Type" : "application/json"}


def mainMenu():
    clear_screen()
    print "ASCII art goes here."
    print "\n\nMain Menu"
    print "---------"
    print "1. Deployment"
    print "2. Create Network"
    print "3. Recent Tasks"
    print "4. Toggle Efficiencies on Container"
    print "5. Change Data Services IP"
    print "6. Get Container Settings"
    print "7. VM Cost Showback"
    print "8. CALM.IO Deployment"
    print "0. Exit"

    mainMenuChoice = raw_input("\n\nMake your selection: ")

    if mainMenuChoice == "1":
        "deployment"
    elif mainMenuChoice == "2":
        createNetwork()
    elif mainMenuChoice == "3":
        "recentTasks"
    elif mainMenuChoice == "4":
        "modifyContainer"
    elif mainMenuChoice == "5":
        "dataServiceIP"
    elif mainMenuChoice == "6":
        "getContainerInfo"
    elif mainMenuChoice == "7":
        "vmCosts"
    elif mainMenuChoice == "8":
        "calmDeploy"
    elif mainMenuChoice == "0":
        clear_screen()
        print "Goodbye ASCII"
    else:
        mainMenu()

def deployment():
    "Nothing here yet."

def createNetwork():
    print "\n\nPlease enter your network option."
    vlan_name = raw_input("\nEnter VLAN name for new network: ")
    vlan_id = int(raw_input("\nEnter VLAN ID for %s network: " % vlan_name))
    body = '{"annotation": "string","ip_config": {"default_gateway": "10.68.70.1","dhcp_options": {"boot_file_name": "boot_file","domain_name": "domain","domain_name_servers": "10.68.70.1","domain_search": "domain","tftp_server_name": "tftp"},"dhcp_server_address": "10.68.70.2","network_address": "10.68.70.0","pool": [{"range": "10.68.70.10 10.68.70.50"}],"prefix_length": "24"},"logical_timestamp": 0,"name": "%s","vlan_id": %s,"vswitch_name": "br0"}' % (vlan_name, vlan_id)
    resp = requests.post(network_api, headers=headers, verify=verify_SSL, data=body)
    print "\nStatus Code = " + str(resp.status_code)
    print "\n\nCommand completed - please see your new network in PRISM."
    raw_input("\n\nHit enter to return to main menu...")
    mainMenu()



print requests.get(cluster_api, headers=headers, verify=verify_SSL)
mainMenu()


