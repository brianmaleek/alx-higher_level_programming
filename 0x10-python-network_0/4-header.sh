#!/bin/bash
# Script takes in a URL, sends a GET request to the URL, displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
