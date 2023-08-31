#!/bin/bash
# 5. cURL POST parameters   
curl -s -d "email: test@gmail.com&subject: I will always be here for PLD" -X POST $1
