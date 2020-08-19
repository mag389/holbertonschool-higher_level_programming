#!/bin/bash
# sends delete request
curl -sIo /dev/null -w "%{http_code}" "$1"
