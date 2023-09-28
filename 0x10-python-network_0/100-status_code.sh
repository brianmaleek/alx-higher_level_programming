#!/bin/bash
# Script takes in a URL, displays status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
