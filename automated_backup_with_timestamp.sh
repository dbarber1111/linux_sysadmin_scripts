#!/bin/bash

# Create backups of your critical files and directories with this script, which appends a timestamp to the backup file

SOURCE="/path/to/your/important/files"
DESTINATION="/path/to/your/backup/directory"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
tar czf "${DESTINATION}/backup_${TIMESTAMP}.tar.gz" "${SOURCE}"