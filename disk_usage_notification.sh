#!/bin/bash

# Receive notifications when disk usage exceeds a certain threshold

THRESHOLD=90
EMAIL="your-email@example.com"
PARTITION="/"

USAGE=$(df -h "${PARTITION}" | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "${USAGE}" -gt "${THRESHOLD}" ]; then
    echo "Disk usage on ${PARTITION} is at ${USAGE}%. Consider freeing up some space." | mail -s "Disk Usage Alert" "${EMAIL}"
fi