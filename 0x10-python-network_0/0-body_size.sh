#!/bin/bash
#Sends the request to URL and desplay size of the body
curl -s "$1" | wc -c
