#!/bin/bash
# 0. cURL body size
curl -i -s "$1" | grep -i 'Content-Length' | cut -d " " -f2
