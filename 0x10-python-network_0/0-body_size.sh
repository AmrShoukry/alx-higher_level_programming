#!/bin/bash
# 0. cURL body size
curl -i -s 0.0.0.0:5000 | grep -i 'Content-Length' | cut -d " " -f2
