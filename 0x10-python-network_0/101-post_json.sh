#!/bin/bash
# sends POST request with a file
curl -sX "POST" "$1" -d@"$2" -H "Content-Type: application/json"
