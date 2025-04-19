#!/bin/bash

# Keep track of your server’s system load and resource usage

echo "System Load: $(uptime)"
echo "Free Memory: $(free -h | grep Mem | awk '{print $4}')"
echo "Free Disk Space: $(df -h / | grep / | awk '{print $4}')"
echo "Total Disk Space: $(df -h / | grep / | awk '{print $2}')"