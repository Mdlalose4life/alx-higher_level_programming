#!/bin/bash
#Displays all HTTP methods the sever accepts
curl -sI "$s1" | grep "Allow" | cut -d " " -f 2-
