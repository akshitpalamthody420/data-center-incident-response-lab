# Incident 04: High CPU Usage

## Severity
Low to Medium

## Symptom
Monitoring shows increased CPU usage on the host or a container.

## Simulate the issue

```bash
python3 scripts/generate_cpu_load.py
```

## Diagnosis

```bash
docker stats
top
```

Open Grafana at `http://localhost:3000` and view the Docker Server Overview dashboard.

## Root cause
A CPU-intensive process was running locally to simulate load.

## Fix
Wait for the script to finish or stop the process.

## Verification

```bash
docker stats
python3 scripts/healthcheck.py
```

Expected result: CPU usage returns to normal.
