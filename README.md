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
│
├── microservices/                # Application source code
│   ├── product-service/           # Manages products
│   │   ├── src/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── order-service/             # Handles orders
│   ├── cart-service/              # User cart logic
│   └── payment-service/           # Simulated payments
│
├── infra/                         # Infrastructure as Code (IaC)
│   ├── terraform/                 # AWS infra provisioning
│   ├── kubernetes/                # YAML files for K8s/EKS
│   └── docker-compose.yml         # Local dev setup
│
├── cicd/                          # CI/CD Pipelines
│   ├── jenkins/
│   │   └── Jenkinsfile
│   └── gitlab-ci.yml
│
├── monitoring/                    # Observability stack
│   ├── prometheus/
│   ├── grafana/
│   └── elk-stack/
│
├── docs/                          # Documentation + Diagrams
│   ├── architecture.png
│   ├── workflow.md
│   └── screenshots/
│
└── README.md                      # Project overview


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
