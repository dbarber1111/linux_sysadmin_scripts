#!/bin/bash

# Monitor failed SSH login attempts and receive notifications

LOG_FILE="/var/log/auth.log"
EMAIL="your-email@example.com"
FAILED_ATTEMPTS=$(grep -c "Failed password" "${LOG_FILE}")

if [ "${FAILED_ATTEMPTS}" -gt 0 ]; then
    echo "There have been ${FAILED_ATTEMPTS} failed SSH login attempts." | mail -s "SSH Login Alert" "${EMAIL}"
fi