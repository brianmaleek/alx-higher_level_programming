#!/bin/bash
# Script takes in a URL, displays status code of the response
curl -s -o "$1" /dev/null -w "%{http_code}"
