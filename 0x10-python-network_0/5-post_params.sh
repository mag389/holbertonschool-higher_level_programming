#!/bin/bash
# get requets with header var
curl -sL -X "POST" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
