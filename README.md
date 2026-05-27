# Data Center Incident Response Lab

A local infrastructure lab that simulates a small data center environment using Docker.

This project runs multiple server-like services on a laptop, monitors them, checks their health, and includes incident reports showing how common infrastructure problems can be diagnosed and fixed.

It is designed to demonstrate practical server troubleshooting skills such as service checks, container inspection, log review, health monitoring, and incident documentation.

## What This Project Does

This project creates a mini data center-style environment with:

- **Nginx** as a web server
- **PostgreSQL** as a database service
- **Prometheus** for monitoring
- **Grafana** for dashboards
- **cAdvisor** for container resource metrics
- **Python health-check scripts** for checking service status
- **Incident reports** for simulated infrastructure failures

The main goal is to practise this workflow:

```text
Start services
    ↓
Check whether they are healthy
    ↓
Simulate an infrastructure issue
    ↓
Investigate using terminal commands and logs
    ↓
Fix the issue
    ↓
Verify the system is healthy again
    ↓
Document the incident
```

## Why This Project Is Useful

In a data center or infrastructure role, technicians often need to check whether servers and services are running correctly, diagnose failures, follow troubleshooting steps, and document fixes.

This project demonstrates those skills in a local environment by simulating problems such as:

- A web server going down
- A database service being unavailable
- Port or connectivity issues
- High CPU usage
- Disk pressure
- Container health problems

## Services Included

| Service | URL | Purpose |
|---|---|---|
| Nginx | `http://localhost:8080` | Local web server |
| Prometheus | `http://localhost:9090` | Monitoring system |
| Grafana | `http://localhost:3000` | Dashboard interface |
| cAdvisor | `http://localhost:8081` | Container metrics |
| PostgreSQL | port `5432` | Database service |

Grafana login:

```text
Username: admin
Password: admin
```

## Project Structure

```text
data-center-incident-response-lab/
  docker-compose.yml
  README.md

  nginx/
    index.html
    nginx.conf

  prometheus/
    prometheus.yml

  grafana/
    provisioning/

  scripts/
    healthcheck.py
    generate_cpu_load.py
    fill_disk_space.sh

  incidents/
    01-web-server-down.md
    02-port-conflict.md
    03-database-unavailable.md
    04-high-cpu.md
    05-disk-pressure.md

  docs/
    troubleshooting-playbook.md
    linux-networking-cheatsheet.md

  screenshots/
```

## What Each Part Does

### `docker-compose.yml`

Defines and starts all services in the lab.

Instead of starting each service manually, this file allows the whole environment to be started with:

```bash
docker compose up -d
```

It creates the local web server, database, monitoring tools, dashboard, and container metrics service.

### `nginx/`

Contains the files for the local web server.

- `index.html` is the webpage served at `http://localhost:8080`
- `nginx.conf` contains the Nginx server configuration

This service is used to simulate a basic server that should stay online.

### `prometheus/prometheus.yml`

Configures Prometheus.

Prometheus collects monitoring data from available services and shows whether configured targets are up or down.

The Prometheus targets page can be viewed at:

```text
http://localhost:9090/targets
```

### `grafana/`

Contains Grafana provisioning files.

Grafana is used to display monitoring data in dashboards. It connects to Prometheus as a data source.

Grafana can be opened at:

```text
http://localhost:3000
```

### `scripts/healthcheck.py`

Runs checks against the lab and prints a JSON-style health report.

It checks things such as:

- Whether the web server is reachable
- Whether Prometheus is reachable
- Whether Grafana is reachable
- Whether cAdvisor is reachable
- Whether expected Docker containers are running
- Whether PostgreSQL is available

Run it with:

```bash
python3 scripts/healthcheck.py
```

Example output:

```json
{
  "overall_status": "PASS",
  "checks": [
    {
      "name": "web_server_http",
      "status": "PASS",
      "details": "HTTP 200 OK"
    },
    {
      "name": "container_dc-lab-prometheus",
      "status": "PASS",
      "details": "running"
    }
  ]
}
```

### `scripts/generate_cpu_load.py`

Simulates a high CPU incident for a short period of time.

Run it with:

```bash
python3 scripts/generate_cpu_load.py
```

It intentionally keeps the CPU busy for about 30 seconds. This can be used to practise checking resource usage with commands such as:

```bash
docker stats
top
```

### `scripts/fill_disk_space.sh`

Simulates disk pressure by creating a temporary file.

This is used to practise disk troubleshooting with commands such as:

```bash
df -h
du -sh *
```

### `incidents/`

Contains incident reports written like basic infrastructure tickets.

Each incident explains:

- What the problem was
- How it was detected
- Commands used during investigation
- Root cause
- Fix
- Verification
- Prevention ideas

These reports demonstrate a structured troubleshooting workflow.

### `docs/`

Contains supporting notes and command references.

Examples:

- Linux troubleshooting commands
- Network debugging commands
- Common checks for services, ports, logs, and disk usage

### `screenshots/`

Stores screenshots showing the lab running.

Useful screenshots include:

- Docker containers running
- Health-check output
- Nginx web server page
- Prometheus targets page
- Grafana dashboard
- cAdvisor metrics page

## Requirements

Install:

- Docker Desktop
- Python 3

Check Docker is installed:

```bash
docker --version
docker compose version
```

Check Python is installed:

```bash
python3 --version
```

## Setup

Clone the repository:

```bash
git clone <your-repo-url>
cd data-center-incident-response-lab
```

Start the lab:

```bash
docker compose up -d
```

Check running containers:

```bash
docker compose ps
```

Run the health check:

```bash
python3 scripts/healthcheck.py
```

Open the services:

```text
Nginx:      http://localhost:8080
Prometheus: http://localhost:9090
Grafana:    http://localhost:3000
cAdvisor:   http://localhost:8081
```

## How To Test the Lab

### 1. Check all services are running

```bash
docker compose ps
```

Expected result: the main containers should show as running.

### 2. Check the web server

```bash
curl -I http://localhost:8080
```

Expected result:

```text
HTTP/1.1 200 OK
```

### 3. Run the health-check script

```bash
python3 scripts/healthcheck.py
```

Expected result: the overall status should be `PASS`.

### 4. Open Prometheus targets

Go to:

```text
http://localhost:9090/targets
```

Expected result: configured targets should show as `UP`.

### 5. Open Grafana

Go to:

```text
http://localhost:3000
```

Login with:

```text
admin / admin
```

## Example Incident: Web Server Down

Stop the web server:

```bash
docker stop dc-lab-web-server
```

Check the issue:

```bash
curl -I http://localhost:8080
python3 scripts/healthcheck.py
docker compose ps
```

Expected result: the health check should report a failure for the web server.

Fix the issue:

```bash
docker start dc-lab-web-server
```

Verify the fix:

```bash
curl -I http://localhost:8080
python3 scripts/healthcheck.py
```

The web server should return `HTTP 200 OK` again.

This demonstrates a basic incident response workflow:

```text
Service unavailable
    ↓
Health check fails
    ↓
Container status checked
    ↓
Service restarted
    ↓
Endpoint verified
```

## Example Incident: High CPU

Run:

```bash
python3 scripts/generate_cpu_load.py
```

While it is running, open another terminal and check resource usage:

```bash
docker stats
```

or:

```bash
top
```

The script runs for about 30 seconds and then stops.

This simulates a temporary resource pressure incident.

## Example Incident: Database Unavailable

Stop PostgreSQL:

```bash
docker stop dc-lab-postgres
```

Run:

```bash
python3 scripts/healthcheck.py
docker compose ps
```

Restart PostgreSQL:

```bash
docker start dc-lab-postgres
```

Verify:

```bash
python3 scripts/healthcheck.py
```

## Stopping the Lab

To stop all services:

```bash
docker compose down
```

To stop and remove volumes as well:

```bash
docker compose down -v
```

Only use `-v` if you are happy to delete stored Grafana/PostgreSQL data.

## Troubleshooting

### Docker says a port is already in use

Check what is using the port:

```bash
lsof -i :8080
```

Then either stop that process or change the port in `docker-compose.yml`.

### A container is not running

Check container status:

```bash
docker compose ps
```

Check logs:

```bash
docker logs <container-name>
```

Example:

```bash
docker logs dc-lab-web-server
```

### Prometheus or Grafana is not loading

Check containers:

```bash
docker compose ps
```

Check logs:

```bash
docker logs dc-lab-prometheus
docker logs dc-lab-grafana
```

### Health check fails

Run:

```bash
docker compose ps
```

Then inspect the failing service with:

```bash
docker logs <container-name>
```

## Skills Demonstrated

This project demonstrates:

- Docker and Docker Compose
- Local server deployment
- Web server troubleshooting
- Database service checks
- Monitoring with Prometheus
- Dashboards with Grafana
- Container metrics with cAdvisor
- Python health-check scripting
- Linux/networking command usage
- Incident documentation
- Root cause analysis and verification

