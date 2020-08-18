#!/usr/bin/env bash
# gedy size of freponse from given url
if [ $# -lt 2 ]
then
	echo "no ip given"
else
	curl "$1" | wc -c
fi
