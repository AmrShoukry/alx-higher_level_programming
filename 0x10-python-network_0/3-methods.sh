#!/bin/bash
# 3. cURL only methods
curl -s -I $1 | grep "Allow" | cut -d ":" -f2 | cut -c2-
