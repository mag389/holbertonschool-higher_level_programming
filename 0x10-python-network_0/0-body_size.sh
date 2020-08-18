#!/usr/bin/env bash
# gedy size of freponse from given url
curl -s "$1" | wc -c
