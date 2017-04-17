#!/bin/bash
# This is my bash scrip to get program information and send
# to an email whenever the pi is powered up, rebooted, or logged into.

# I like to set the file to sleep for 10 seconds that way there is enough
# time to establish network connection and get dhcp assigned ip.
sleep 10

# Now a line to get information and filter through grep and email.
