#!/bin/bash

# Monitor your SSL certificate expiration dates and receive notifications

DOMAIN="yourdomain.com"
EMAIL="your-email@example.com"
DAYS_THRESHOLD=30

EXPIRATION_DATE=$(echo | openssl s_client -servername "${DOMAIN}" -connect "${DOMAIN}:443" 2>/dev/null | openssl x509 -enddate -noout | awk -F= '{print $2}')
EXPIRATION_SECONDS=$(date -d "${EXPIRATION_DATE}" +%s)
CURRENT_SECONDS=$(date +%s)
SECONDS_DIFFERENCE=$((EXPIRATION_SECONDS - CURRENT_SECONDS))
DAYS_DIFFERENCE=$((SECONDS_DIFFERENCE / 86400))

if [ "${DAYS_DIFFERENCE}" -lt "${DAYS_THRESHOLD}" ]; then
    echo "The SSL certificate for ${DOMAIN} will expire in ${DAYS_DIFFERENCE} days (${EXPIRATION_DATE})." | mail -s "SSL Certificate Expiration Alert" "${EMAIL}"
fi