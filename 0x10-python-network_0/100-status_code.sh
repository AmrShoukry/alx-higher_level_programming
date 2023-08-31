#!/bin/bash
# 7. Only status code   
curl -s -L -w "%{http_code}" -o /dev/null $1
