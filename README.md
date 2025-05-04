# Dependency Auto-Updater with Kubernetes Deployment

## Overview

This project demonstrates an **automated system** for keeping Docker container dependencies up to date, automatically rebuilding and redeploying a **Flask-based API** application to a **Kubernetes cluster** using **GitHub Actions**, **Renovate Bot**, and **Minikube**.

---

## Features

- **Automated Dependency Scanning** via Renovate Bot
- **CI/CD Pipeline** with GitHub Actions:
  - Pull Request triggered builds
  - Docker image rebuilds and push
  - Unit testing for Flask API
- **Container Registry Integration** (e.g., DockerHub or GitHub Container Registry)
- **Automatic Kubernetes Rollout** using `kubectl apply`
- Local cluster simulation using **Minikube**

---

## Technologies Used

- [Flask](https://flask.palletsprojects.com/) – lightweight Python web framework
- [Docker](https://www.docker.com/) – containerization of the Flask API
- [GitHub Actions](https://docs.github.com/en/actions) – automation pipeline
- [Renovate Bot](https://docs.renovatebot.com/) – dependency update automation
- [Kubernetes](https://kubernetes.io/) – container orchestration
- [Minikube](https://minikube.sigs.k8s.io/) – local Kubernetes cluster

---

## Project Structure

```

.
├── .github/
│   └── workflows/
│       └── docker-image.yml             # GitHub Actions workflow
├── Dockerfile                           # Flask app Dockerfile
├── deployment.yaml                      # Kubernetes Deployment + Service
├── app/
│   └── app.py                           # Flask app with GET and POST endpoints
|   └── test_app.py  
├── renovate.json                        # Renovate Bot configuration
└── README.md

````

---

## Flask API

**GET /external**

Returns a simple GET response of https://api.github.com/

**POST /items**

Accepts a JSON payload and checks it against expected format. Returns a success or failure message based on validation.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Kej-r03/dockmate.git
cd dockmate
````

---

### 2. Configure Renovate Bot


* Enable Renovate on your GitHub repo by installing the GitHub App from [https://github.com/apps/renovate](https://github.com/apps/renovate)

Renovate will now scan `Dockerfile` and create PRs when dependencies (e.g., Python base images) are outdated.

---

### 3. Setup Minikube

Ensure Minikube and kubectl are installed.

```bash
minikube start
```

---

### 4. Build and Push Docker Image

Set up GitHub Secrets:

* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`


GitHub Actions (`.github/workflows/docker-image.yml`) will:

* Build and test the image
* Push to container registry
* Apply new image to Kubernetes using `kubectl` (Here, we're using local minikube cluster)

---

### 5. Deploy to Kubernetes

Deploy with:

```bash
kubectl apply -f deployment.yaml
kubectl get pods
minikube service dockmate-service
```

---

## Workflow Summary

1. **Renovate Bot** scans `Dockerfile`.
2. If updates exist, it creates a PR.
3. **GitHub Actions** triggers on PR merge:

   * Runs tests
   * Builds and pushes Docker image
   * Deploys to Kubernetes using `kubectl apply`
4. **Minikube** reflects changes in local cluster.

---

## Sample API Requests

**GET:**

```bash
curl http://<minikube-ip>:<node-port>/external
```

**POST:**

```bash
curl -X POST http://<minikube-ip>:<node-port>/items \
     -H "Content-Type: application/json" \
     -d  '{"name": "Laptop", "description": "A powerful machine", "price": 999.99}'
```

---

