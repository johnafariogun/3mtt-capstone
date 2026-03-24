Crypto Streaming Pipeline 

A real-time data engineering pipeline that ingests live cryptocurrency prices, processes them with Spark, and stores them in a highly available Cassandra cluster.

Architecture
The pipeline follows a modern distributed data architecture:
1. **Ingestion**: Python-based WebSocket client fetching live data from CoinCap/Binance.
2. **Buffering**: Apache Kafka handles the message stream to ensure fault tolerance.
3. **Processing**: Apache Spark Structured Streaming consumes Kafka topics for real-time transformations.
4. **Storage**: Apache Cassandra (NoSQL) stores the processed time-series data for fast querying.



---

## Tech Stack
* **Language:** Python 3.x
* **Stream Ingestion:** WebSockets (`websocket-client`)
* **Message Broker:** Apache Kafka
* **Stream Processing:** Apache Spark (PySpark)
* **Database:** Apache Cassandra
* **Containerization:** Docker & Docker Compose (Kubernetes maybe)

---

## Getting Started

### 1. Prerequisites
Ensure you have the following installed:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Python 3.9+](https://www.python.org/downloads/)

### 2. Setup Environment
Clone the repository and install the local Python dependencies:
```bash
pip install websocket-client confluent-kafka cassandra-driver
```

### 3. Start the Infrastructure
Run the following command to spin up Kafka, Zookeeper, and Cassandra:
```bash
docker-compose up -d
```

### 4. Run the Pipeline
1. **Start the Producer**: 
   `python src/producer.py`
2. **Start the Spark Job**: 
   `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.x.x src/spark_stream.py`

---

## Data Schema
The data is gotten from coincap websocket provisionally and is then stored in the `crypto_keyspace.price_stream` table with the following structure:

| Column | Type | Description |
| :--- | :--- | :--- |
| `coin_id` | TEXT | Partition Key (e.g., bitcoin) |
| `trade_time` | TIMESTAMP | Clustering Column (Sorted DESC) |
| `price` | DECIMAL | Live USD Price |

---

## Roadmap
- WebSocket Producer Implementation ✅
- Kafka Integration
- Spark Structured Streaming Logic
- Cassandra Data Sink
- Dashboard Visualization (Grafana/Streamlit)


