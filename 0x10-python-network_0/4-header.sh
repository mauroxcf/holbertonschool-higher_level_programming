#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL, sending X-HolbertonSchool-User-Id with value 98
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
