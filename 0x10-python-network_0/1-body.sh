#!/usr/bin/env bash
# sends get displays body
if [ $# -lt 1 ]
then
	echo "no ip given"
else
	curl -sL "$1"
fi
