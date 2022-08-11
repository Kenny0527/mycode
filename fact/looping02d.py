#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption.
         Sort domains ending in .org and .com into files
         org-domain.txt and com-domain.txt."""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n')

        # IF the string svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
