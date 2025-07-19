🗨️ Web Chat Application

A minimal, real-time web chat platform built to be containerized and deployed effortlessly using Docker. 
This application is ideal for learning backend/frontend integration, real-time communication, and Docker-based deployment workflows.
---
📌 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Setup Instructions](#-setup-instructions)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Clone Repository](#2-clone-repository)
  - [3. Setup Environment Variables (Optional)](#3-setup-environment-variables-optional)
  - [4. Build Docker Image](#4-build-docker-image)
  - [5. Run Docker Container](#5-run-docker-container)
  - [6. Access the Application](#6-access-the-application)
- [Docker Commands](#-docker-commands)
- [Deployment on EC2](#-deployment-on-ec2)
- [Running Multiple Containers](#-running-multiple-containers)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Maintainer](#-maintainer)
---
📖 Overview
This project is a real-time chat system where users can send and receive messages instantly with in the group. 
It's built with clean separation between server and client logic, and is packaged into a Docker container for consistent deployment in any environment.
---
🧱 Architecture
Client (Browser) ↓ WebSocket/HTTP Server (Express/Fastify/Flask/etc.) ↓ Docker Container ↓ EC2 / Render / Any Cloud Instance
The application listens on an internal container port (e.g., 8000) which is mapped to an external port (e.g., 10000) on the host machine or cloud VM for public access.
---
🧰 Tech Stack

- **Backend:** Node.js / Express (or your backend)
- **Real-time:** Socket.io or WebSocket (if applicable)
- **Frontend:** HTML/CSS/JavaScript (React/Vue optional)
- **Containerization:** Docker
- **Deployment:** EC2 / Render / DockerHub
---
⚙️ Setup Instructions

1. Prerequisites

- Docker installed on your local or cloud machine.
- (Optional) AWS EC2 instance with Docker installed.
- Internet access and basic command-line knowledge.

2. Repository

```bash
(https://github.com/GITHUB-SUBASHk/web-chat.git)
3. Setup Environment Variables (Optional)

If your app uses environment variables, create a .env file:

# .env file
PORT=8000
DB_URL=mongodb://localhost:27017/webchat
NODE_ENV=production

> Make sure your Dockerfile supports copying .env or uses a .dockerignore correctly.

4. Build Docker Image

docker build -t web-chat .
Optional tagging for Docker Hub:
docker tag web-chat dkrsubashk/web-chat:latest
docker push dkrsubashk/web-chat:latest

5. Run Docker Container
docker run -d -p 10000:8000 --name web-chat web-chat
10000 is the public port exposed by the host (EC2 or local)
8000 is the internal app port your server listens to
change the expose port if conflicts araise 

6. Access the Application
Open in browser:
http://<your-public-ip>:10000
---
🐳 USE Docker

Clone the repo from github:

Install docker and
Build the image
Run the containeer

(eg:)
List all Docker images:
docker images

List all running containers:
docker ps

List all containers (including stopped):
docker ps -a

---

☁️ Deployment on LOCAL MACHINE
Security Group Configuration:
Open port 10000 (or your chosen host port) in the Security Group
Open SSH (port 22) for admin access
Running on SEREVR:
sudo docker build -t web-chat .
sudo docker run -d -p 10000:8000 web-chat
Access:
http://<public-ip>:10000
> Make sure port 10000 is not used by another service.
---
🧑‍💻 Maintainer

SUBASH K
Email: eng.subashk6@gmail.com
---
📄 License
This project is licensed under the MIT License.

🙌 Contributing

Contributions are welcome. Please fork the repo and create a pull request. For major changes, please open an issue first to discuss the proposed change.
---

Let me know if you want:
- GitHub Actions CI/CD included
- Auto-deploy to Render/DockerHub
- Support for Docker Compose
- NGINX reverse proxy setup
- Database integration (MongoDB, Redis)

I'll tailor it further if your app stack (Node, Flask, etc.) is clarified.


