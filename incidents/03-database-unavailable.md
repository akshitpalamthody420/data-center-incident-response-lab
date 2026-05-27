# Incident 03: Database Unavailable

## Severity
High

## Symptom
The health check reports that PostgreSQL is unavailable on port `5432`.

## Simulate the issue

```bash
docker compose stop postgres
```

## Diagnosis

```bash
docker compose ps
docker logs dc-lab-postgres
python3 scripts/healthcheck.py
```

## Root cause
The PostgreSQL container was stopped, so the database port was unreachable.

## Fix

```bash
docker compose start postgres
```

## Verification

```bash
docker compose ps
python3 scripts/healthcheck.py
```

Expected result: PostgreSQL container is running and `postgres_port_5432` passes.
