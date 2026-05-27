# Linux and Networking Cheatsheet

| Task | Command |
|---|---|
| Check running containers | `docker compose ps` |
| View container logs | `docker logs <container>` |
| Check HTTP response | `curl -I http://localhost:8080` |
| Check port usage | `lsof -i :8080` |
| Check disk usage | `df -h` |
| Check folder size | `du -sh <folder>` |
| Check DNS resolution | `nslookup amazon.com` |
| Check network reachability | `ping google.com` |
| Monitor container resources | `docker stats` |
| Run full lab health check | `python3 scripts/healthcheck.py` |
