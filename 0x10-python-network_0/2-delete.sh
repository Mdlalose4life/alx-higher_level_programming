#!/bin/bash
#Sends Delete Request to $1 then displays reponse body
curl -s "$1" -X DELETE
