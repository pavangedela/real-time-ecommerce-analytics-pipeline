# Real-Time E-Commerce Analytics Pipeline

## Overview

A real-time data engineering project that processes e-commerce orders using Apache Kafka, Apache Spark Structured Streaming, and Spark SQL.

## Architecture

Producer (Python)
        ->
Apache Kafka
        ->
Spark Structured Streaming
        ->
Parquet Storage
        ->
Spark SQL Analytics

## Technologies Used

- Python
- Apache Kafka
- Apache Spark
- Spark Structured Streaming
- Spark SQL
- Docker
- Parquet

## Features

- Real-time order ingestion
- Kafka message streaming
- Revenue calculation
- Parquet data storage
- Product revenue analytics
- Category sales analytics
- Top customer analytics

## Project Structure

```text
producer/
    order_producer.py

spark/
    spark_consumer.py

hive/
    hive_analysis.py

data/
    processed_orders/
```

## Sample Analytics Results

### Top Products

| Product | Revenue |
|----------|----------|
| Laptop | 2100000 |
| Phone | 1050000 |
| Watch | 132000 |
| Shoes | 38000 |

### Category Sales

| Category | Revenue |
|-----------|----------|
| Electronics | 3150000 |
| Accessories | 132000 |
| Fashion | 38000 |
