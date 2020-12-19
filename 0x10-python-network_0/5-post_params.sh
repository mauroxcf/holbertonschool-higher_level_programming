#!/bin/bash
# sends a POST request to the passed URL by sending email and subject with a value"
curl -sd 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
