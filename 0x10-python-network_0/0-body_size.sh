#!/usr/bin/env bash
# gedy size of freponse from given url
if [ $# -lt 1 ]
then
	echo "no ip given"
else
	curl -s "$1" | wc -c
fi
