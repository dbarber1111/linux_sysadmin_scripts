#!/bin/bash
set -e

PROMETHEUS_URL="http://localhost:9090"
PROMETHEUS_DATA_DIR="/var/lib/prometheus"
BACKUP_DIR="/backup/prometheus"
RETENTION_DAYS=7
TIMESTAMP=$(date +%F_%H-%M-%S)

mkdir -p "$BACKUP_DIR"

echo "Starting Prometheus backup at $(date)"

# Create snapshot
echo "Creating snapshot..."
SNAPSHOT_NAME=$(curl -sS -XPOST ${PROMETHEUS_URL}/api/v1/admin/tsdb/snapshot | jq -r '.data.name')

if [ "$SNAPSHOT_NAME" = "null" ] || [ -z "$SNAPSHOT_NAME" ]; then
  echo "ERROR: Snapshot creation failed. Is --web.enable-admin-api enabled?"
  exit 1
fi

echo "Snapshot created: $SNAPSHOT_NAME"

# Backup snapshot
echo "Compressing snapshot..."
sudo tar -czf "${BACKUP_DIR}/prometheus-snapshot-${TIMESTAMP}.tar.gz" \
  -C "${PROMETHEUS_DATA_DIR}/snapshots" "${SNAPSHOT_NAME}"

# Backup configuration
echo "Backing up configuration..."
sudo tar -czf "${BACKUP_DIR}/prometheus-config-${TIMESTAMP}.tar.gz" \
  /etc/prometheus/

# Cleanup old snapshot
echo "Cleaning up snapshot..."
sudo rm -rf "${PROMETHEUS_DATA_DIR}/snapshots/${SNAPSHOT_NAME}"

# Remove old backups
echo "Removing backups older than ${RETENTION_DAYS} days..."
find "${BACKUP_DIR}" -name "prometheus-*.tar.gz" -mtime +${RETENTION_DAYS} -delete

# Show backup info
echo "Backup completed successfully!"
echo "Files created:"
ls -lh "${BACKUP_DIR}/""${TIMESTAMP}"

# Calculate backup size
TOTAL_SIZE=$(du -sh "${BACKUP_DIR}" | cut -f1)
echo "Total backup directory size: ${TOTAL_SIZE}"