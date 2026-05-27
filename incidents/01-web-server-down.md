# Incident 01: Web Server Down

## Severity
Medium

## Symptom
The web server does not respond at `http://localhost:8080`.

## Simulate the issue

```bash
docker compose stop web-server
```

## Diagnosis

```bash
docker compose ps
curl -I http://localhost:8080
docker logs dc-lab-web-server
python3 scripts/healthcheck.py
```

## Root cause
The Nginx container was stopped, so port `8080` was no longer serving HTTP traffic.

## Fix

```bash
docker compose start web-server
```

## Verification

```bash
curl -I http://localhost:8080
python3 scripts/healthcheck.py
```

Expected result: HTTP 200 from Nginx and a passing web server health check.

## Prevention
Use a health check and monitoring dashboard to detect when the service becomes unavailable.
