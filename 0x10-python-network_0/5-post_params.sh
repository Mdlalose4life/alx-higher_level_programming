#!/bin/bash
#Pots the request to URL then display result body
curl -s -X POST -d "X-School-User-ID: 98" "$1"
