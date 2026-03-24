# 📝 Project Specification: The Autonomous Crypto Sentinel
**Target State:** A self-healing, cloud-native streaming platform with automated provisioning and observability.

---

## 1. Core Data Architecture
The flow of data from the edge (Exchange) to the persistent store (Cassandra).

* **Ingestion Layer:** Python-based WebSocket consumers containerized in Docker.
* **Transport Layer:** **Apache Kafka** cluster (Multi-node) for high-throughput buffering.
* **Processing Layer:** **Apache Spark** (Structured Streaming) for real-time ETL and windowed aggregations.
* **Storage Layer:** **Apache Cassandra** (NoSQL) optimized for time-series write-heavy workloads.

---

## 2. Infrastructure as Code (IaC) & Provisioning
Eliminating manual configuration through automation.

* **Cloud Provider:** **AWS** (VPC, EC2/EKS, S3, IAM).
* **Provisioning:** **Terraform**
    * Modularized code for VPC, Security Groups, and Instance clusters.
    * Remote state management using **S3** and **DynamoDB** for state locking.
* **Configuration Management:** **Ansible**
    * Idempotent playbooks to install Java, Docker, and optimize OS-level networking for Kafka/Cassandra.
    * Automated "Health Check" scripts to verify service status post-deployment.

---

## 3. The DevOps & SRE Pillar
Making the system "Production-Ready."

* **Orchestration:** **Kubernetes (EKS)** * Deploying Spark workers and Kafka brokers as StatefulSets.
* **Observability (The LGTM Stack):**
    * **Prometheus:** Scrape JMX metrics from Spark/Kafka.
    * **Grafana:** Real-time dashboards for consumer lag and system throughput.
    * **Loki:** Centralized log aggregation to debug distributed failures.
* **Security:** 
    * **AWS Secrets Manager:** Externalizing API keys and DB credentials.
    * **VPC Peering/Private Subnets:** Ensuring the Database is not accessible via the public internet.

---

## 4. CI/CD Pipeline Definition
The automated path from `git push` to `production`.

| Stage | Tool | Description |
| :--- | :--- | :--- |
| **Static Analysis** | `Pytest` / `Flake8` | Code linting and unit testing for transformation logic. |
| **Security** | `Trivy` | Scanning Docker images for vulnerabilities before push. |
| **Infra Deploy** | `Terraform` | Automatic `plan` on PR and `apply` on Merge to main. |
| **App Deploy** | `ArgoCD` / `Helm` | GitOps-based deployment to the Kubernetes cluster. |

---

## 5. Success Metrics (KPIs)
* **End-to-End Latency:** < 2 seconds from Trade Event to Cassandra Write.
* **Zero Data Loss:** Verified through Kafka Offset tracking.
* **Disaster Recovery:** Ability to tear down and rebuild the entire stack in < 15 minutes using Terraform.