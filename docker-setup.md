# Docker Setup

## Goal
Containerize the Finance Bot and MongoDB using Docker and Docker Compose for a consistent environment.

## Tasks
- [ ] Task 1: Create `Dockerfile` → Verify: `docker build -t finbot .` succeeds
- [ ] Task 2: Create `docker-compose.yml` → Verify: `docker-compose config` is valid
- [ ] Task 3: Update `config.py` for dynamic host discovery → Verify: Connection works on both local and container
- [ ] Task 4: Verify full stack → Verify: `docker-compose up` shows bot and db logs

## Done When
- [ ] Both bot and MongoDB are running in containers.
- [ ] Bot connects successfully to the containerized MongoDB.
- [ ] Environment variables are correctly passed to the bot container.

## Notes
- Use `python:3.12-slim` for a smaller image.
- MongoDB data should be persisted via a Docker volume.
- Network should be shared between bot and db containers.
