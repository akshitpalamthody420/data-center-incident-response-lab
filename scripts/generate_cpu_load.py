#!/usr/bin/env python3
"""Generate CPU load for a short time to test monitoring dashboards."""

import time

DURATION_SECONDS = 30
end_time = time.time() + DURATION_SECONDS

print(f"Generating CPU load for {DURATION_SECONDS} seconds...")
while time.time() < end_time:
    _ = sum(i * i for i in range(10000))
print("Done.")
