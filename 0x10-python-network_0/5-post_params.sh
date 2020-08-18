#!/bin/bash
# get requets with header var
curl -sL -X "POST" -H "email: hr@holbertonschool.com" -H "subject: I will always be here for PLD" "$1"
