#!/bin/bash
# Sends a POST request to the URL, and displays the body of the response
curl -sX "$1" POST -d "email=test@gmail.com&subject=I will always be here for PLD"
