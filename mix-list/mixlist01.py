#!/usr/bin/bash

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0])

# display the third item in the list
print("The last item in the list (state): " + my_list[2])

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display only the IP addresses on the screen
print("IP Addresses: " + iplist[3] + ", and " + iplist[4])


