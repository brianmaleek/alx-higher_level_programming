#!/bin/bash
# Script makes a request to 0.0.0.0:5000/catch_me.
curl -o /dev/null -s -w "You got me!" 0.0.0.0:5000/catch_me
