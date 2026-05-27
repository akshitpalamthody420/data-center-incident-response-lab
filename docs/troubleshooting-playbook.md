# Troubleshooting Playbook

## Service availability

```bash
curl -I http://localhost:8080
docker compose ps
docker logs dc-lab-web-server
```

## Port checks

```bash
lsof -i :8080
lsof -i :5432
```

## Container health

```bash
docker compose ps
docker stats
python3 scripts/healthcheck.py
```

## Disk checks

```bash
df -h
du -sh *
```

## Network checks

```bash
ping google.com
nslookup amazon.com
curl -I https://aws.amazon.com
```

## Useful recovery commands

```bash
docker compose restart web-server
docker compose restart postgres
docker compose up -d
docker compose down
```
