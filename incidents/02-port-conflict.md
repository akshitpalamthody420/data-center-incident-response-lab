# Incident 02: Port Conflict

## Severity
Medium

## Symptom
The web server cannot start because another process is already using port `8080`.

## Simulate the issue

Stop the stack, start a temporary process on port 8080, then try to restart the stack.

```bash
docker compose down
python3 -m http.server 8080
```

In another terminal:

```bash
docker compose up -d
```

## Diagnosis

```bash
docker compose ps
lsof -i :8080
curl -I http://localhost:8080
```

## Root cause
Port `8080` was already bound by another process, preventing Docker from binding Nginx to that port.

## Fix
Stop the process using port `8080`, then restart Docker Compose.

```bash
# Press Ctrl+C in the terminal running python3 -m http.server
docker compose up -d
```

## Verification

```bash
lsof -i :8080
curl -I http://localhost:8080
python3 scripts/healthcheck.py
```
