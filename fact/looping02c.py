#!/usr/bin/env python3
"""Alta3 Research | RZFreezer
    For - looping across a file opened 'with'
    while also being gentle on memory consumption."""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep th dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:
        # print and end without a newline
        print(svr, end="")
