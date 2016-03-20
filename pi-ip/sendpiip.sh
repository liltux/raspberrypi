#!/bin/bash
# This is my bash scrip to get ip information and send
# to my email whenever the pi is powered up or booted.

# I like to set the file to sleep for 10 seconds that way there is enough
# time to establish connection to router and get dhcp assigned ip.
sleep 10

# Now a line to get ip information and filter through grep and email.
# Comment out the interface you are not looking for an ip on.

#ifconfig | grep -2a eth0 | mail -s "Pi IP" youremail@youremail.domain

ifconfig | grep -2a wlan0 | mail -s "Pi IP" youremail@youremail.domain
