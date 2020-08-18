#!/usr/bin/env bash
# sends delete request
if [ $# -lt 1 ]
then
	echo "no ip given"
else
	curl -X "DELETE" "$1"
fi
