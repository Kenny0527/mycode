#!/usr/bin/bash

proto = ["ssh", "http", "https"]

print(proto)
print(proto[1])

#this line will add d, n, s
proto.extend("dns")
print(proto)

