#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
