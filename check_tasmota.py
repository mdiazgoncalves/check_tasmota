#!/usr/bin/python3

# check_tasmota

# Import required libs for your plugin
import argparse
import requests
# from urllib.parse import quote
from requests.auth import HTTPBasicAuth

# Return codes expected by Nagios
codes = [ 'OK', 'WARNING', 'CRITICAL', 'UNKNOWN' ]

# Create the parser
my_parser = argparse.ArgumentParser(description='Check Tasmota node')

# Add the arguments
my_parser.add_argument('Address', metavar='address', type=str, help='the host ip address')
my_parser.add_argument('-U', "--username", metavar='username', type=str, help='the tasmota api username')
my_parser.add_argument('-P', "--password", metavar='password', type=str, help='the tasmota api password')

# Execute the parse_args() method
args = my_parser.parse_args()

payload = {'cmnd': 'Status%200' }

# if args.username:
#     payload['user']= args.username
#     payload['password']= quote(args.password)

# Check logic starts here

try:
    response = requests.get('http://' + args.Address + '/cm', auth=HTTPBasicAuth(args.username, args.password))
    print(response.text)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException  as e:
    status = 2
    message =str(e)
else:
    status = 0
    message = "name:{} mac_address:{} version:{}".format(data['Status']['DeviceName'],data['StatusNET']['Mac'],data['StatusFWR']['Version'])

# Print the message for nagios
print("{} - {}".format(codes[status], message))

# Exit with status code
raise SystemExit(status)
