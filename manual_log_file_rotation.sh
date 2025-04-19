#!/bin/bash
# Prevent log files from growing too large by automating log file rotation

LOG_FILE="/path/to/your/logfile.log"
MAX_SIZE=10485760 # 10 MB
CURRENT_SIZE=$(wc -c <"${LOG_FILE}")

if [ "${CURRENT_SIZE}" -gt "${MAX_SIZE}" ]; then
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    mv "${LOG_FILE}" "${LOG_FILE}_${TIMESTAMP}"
    touch "${LOG_FILE}"
fi