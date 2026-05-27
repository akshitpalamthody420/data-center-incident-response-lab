# Incident 05: Disk Pressure / Log Growth

## Severity
Medium

## Symptom
Disk usage is increasing due to generated files or log growth.

## Simulate the issue

```bash
./scripts/fill_disk_space.sh
```

## Diagnosis

```bash
df -h
du -sh tmp/*
python3 scripts/healthcheck.py
```

## Root cause
A large temporary file was created in the project `tmp/` folder.

## Fix

```bash
rm tmp/simulated-large-log.bin
```

## Verification

```bash
df -h
du -sh tmp || true
python3 scripts/healthcheck.py
```

Expected result: disk usage is reduced and the large temporary file is gone.
