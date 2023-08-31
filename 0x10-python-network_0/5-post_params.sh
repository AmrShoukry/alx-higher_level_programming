#!/bin/bash
# 5. cURL POST parameters   
curl -s -d "email: test@gmail.com" -d "subject: I will always be here for PLD" -X POST -i $1| grep -A20030803 "POST params:"
