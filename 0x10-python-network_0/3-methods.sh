#!/usr/bin/env bash
# sends delete request
if [ $# -lt 1 ]
then
	echo "no ip given"
else
	curl -sI "$1" | grep "Allow:" | cut -d" " -f 2-11
fi
