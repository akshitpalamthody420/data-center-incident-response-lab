#!/usr/bin/env bash
set -euo pipefail

mkdir -p tmp
# Creates a small 50MB file to simulate log/disk growth safely.
dd if=/dev/zero of=tmp/simulated-large-log.bin bs=1m count=50

echo "Created tmp/simulated-large-log.bin"
echo "Remove it with: rm tmp/simulated-large-log.bin"
