#!/bin/bash
# This script takes a URL as input and displays

url=$1 size=$(curl -si $url | awk '/Content-Length/{print $2}') echo $size
