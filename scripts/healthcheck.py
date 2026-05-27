#!/usr/bin/env python3
"""Simple infrastructure health check script for the Data Center Incident Response Lab."""

from __future__ import annotations

import json
import shutil
import socket
import subprocess
import sys
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class CheckResult:
    name: str
    status: str
    details: str


def check_http(url: str) -> CheckResult:
    try:
        with urllib.request.urlopen(url, timeout=3) as response:
            if 200 <= response.status < 400:
                return CheckResult("web_server_http", "PASS", f"{url} returned HTTP {response.status}")
            return CheckResult("web_server_http", "FAIL", f"{url} returned HTTP {response.status}")
    except Exception as exc:  # noqa: BLE001 - useful for a CLI health report
        return CheckResult("web_server_http", "FAIL", str(exc))


def check_port(host: str, port: int, name: str) -> CheckResult:
    try:
        with socket.create_connection((host, port), timeout=3):
            return CheckResult(name, "PASS", f"{host}:{port} is reachable")
    except OSError as exc:
        return CheckResult(name, "FAIL", f"{host}:{port} is not reachable: {exc}")


def check_disk(threshold_percent: int = 90) -> CheckResult:
    usage = shutil.disk_usage("/")
    used_percent = round((usage.used / usage.total) * 100, 2)
    status = "PASS" if used_percent < threshold_percent else "WARN"
    return CheckResult("disk_usage", status, f"Root disk usage is {used_percent}%")


def check_docker_container(container_name: str) -> CheckResult:
    try:
        result = subprocess.run(
            ["docker", "inspect", "-f", "{{.State.Running}}", container_name],
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode != 0:
            return CheckResult(f"container_{container_name}", "FAIL", result.stderr.strip())
        running = result.stdout.strip() == "true"
        return CheckResult(
            f"container_{container_name}",
            "PASS" if running else "FAIL",
            "running" if running else "not running",
        )
    except Exception as exc:  # noqa: BLE001
        return CheckResult(f"container_{container_name}", "FAIL", str(exc))


def main() -> int:
    checks = [
        check_http("http://localhost:8080/health"),
        check_port("localhost", 8080, "nginx_port_8080"),
        check_port("localhost", 5432, "postgres_port_5432"),
        check_port("localhost", 9090, "prometheus_port_9090"),
        check_port("localhost", 3000, "grafana_port_3000"),
        check_disk(),
        check_docker_container("dc-lab-web-server"),
        check_docker_container("dc-lab-postgres"),
        check_docker_container("dc-lab-prometheus"),
        check_docker_container("dc-lab-grafana"),
    ]

    overall = "PASS" if all(check.status == "PASS" for check in checks) else "ATTENTION_REQUIRED"
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "overall_status": overall,
        "checks": [asdict(check) for check in checks],
    }
    print(json.dumps(report, indent=2))
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
