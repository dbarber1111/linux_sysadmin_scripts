#!/bin/bash
GRAFANA_URL="http://grafana.local"
API_TOKEN="YOUR_TOKEN"
BACKUP_DIR="/backup/grafana"
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +%F_%H-%M-%S)

# Get all dashboard UIDs
DASHBOARD_UIDS=$(curl -sS -H "Authorization: Bearer ${API_TOKEN}" \
  "${GRAFANA_URL}/api/search?type=dash-db" | jq -r '.[].uid')

# Backup each dashboard
for uid in $DASHBOARD_UIDS; do
  echo "Backing up dashboard: $uid"
  curl -sS -H "Authorization: Bearer ${API_TOKEN}" \
    "${GRAFANA_URL}/api/dashboards/uid/${uid}" \
    > "${BACKUP_DIR}/dashboard-${uid}-${TIMESTAMP}.json"
done

echo "All dashboards backed up to ${BACKUP_DIR}"