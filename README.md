# 🛒 E-Commerce Microservices with DevOps

## 📌 Project Overview
This is a **microservices-based E-Commerce platform** built with modern **DevOps practices**.  
It simulates core features like **Products, Orders, Cart, and Payments**.

## 🛠 Tools & Technologies
- **Programming:** Python Flask, Node.js
- **Containerization:** Docker, Docker Compose
- **Orchestration:** Kubernetes (EKS)
- **IaC:** Terraform (AWS)
- **CI/CD:** Jenkins / GitHub Actions
- **Monitoring:** Prometheus, Grafana, ELK
- **Version Control:** Git & GitHub

## 🏗 Architecture
![Architecture Diagram](docs/architecture.png)

## 📂 Project Layout
ecommerce-microservices-devops/
├── microservices/ # Product, Order, Cart, Payment services
├── infra/ # Terraform + K8s manifests
├── cicd/ # Jenkinsfile / GitHub Actions
├── monitoring/ # Prometheus, Grafana, ELK configs
└── README.md # Project overview


## 🚀 Quick Start (Local with Docker)
```bash
cd microservices/product-service
docker build -t product-service:1.0 .
docker run -d -p 5001:5001 product-service:1.0
curl http://localhost:5001/products

📌 Roadmap

 Product Service (Flask + Docker)

 Cart Service

 Order Service

 Payment Service

 Docker Compose for local testing

 CI/CD pipeline with Jenkins

 Terraform for AWS EKS

 Kubernetes deployment

 Monitoring (Prometheus + Grafana)

👨‍💻 Author
Vimala  – AWS DevOps Enthusiast 🚀
***************************************************
## 🐞 Troubleshooting

### 🔹 1. Port Already Allocated
If you see an error like:
Error response from daemon: Bind for 0.0.0.0:5001 failed: port is already allocated

makefile
Copy code
👉 This means another container is already using that port.

✅ Fix:
```bash
# Stop all running containers
docker stop $(docker ps -q)

# Remove all stopped containers
docker rm $(docker ps -aq)

# Restart the stack
docker compose up -d --build
🔹 2. Old Images Not Updating
If code changes don’t reflect inside the container:

bash
Copy code
docker compose build --no-cache
docker compose up -d
🔹 3. Check Logs of a Service
bash
Copy code
docker logs -f product-service
🔹 4. Verify All Services Running
bash
Copy code
docker ps
Expected:

Product Service → http://localhost:5001/products

Cart Service → http://localhost:5002/

Order Service → http://localhost:5003/

Payment Service → http://localhost:5004/

