#!/bin/bash
# 7. Only status code   
curl -s -L -o /dev/null -w "%{http_code}" $1
