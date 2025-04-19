#!/bin/bash

# Automatically monitor and restart essential services if they go down

SERVICE="your-service-name"
EMAIL="your-email@example.com"

if systemctl is-active --quiet "${SERVICE}"; then
    echo "${SERVICE} is running."
else
    echo "${SERVICE} is not running. Restarting..." | mail -s "${SERVICE} Restart Alert" "${EMAIL}"
    systemctl start "${SERVICE}"
fi