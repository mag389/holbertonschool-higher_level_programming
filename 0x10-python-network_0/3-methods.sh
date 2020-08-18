#!/usr/bin/env bash
# sends delete request
curl -sI "$1" | grep "Allow:" | cut -d" " -f 2-11
