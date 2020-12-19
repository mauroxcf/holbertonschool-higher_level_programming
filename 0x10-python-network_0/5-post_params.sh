#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL by sending email and subject with a value"
curl -sX POST -F 'email=hr@holbertonschool.com' -F 'subject=I will always be here for PLD' "$1"
