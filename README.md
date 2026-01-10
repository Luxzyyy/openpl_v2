# OpenPowerlifting Analytics
**End-to-End Data Engineering & BI Project**

This repository showcases an end-to-end analytics project built on top of the [OpenPowerlifting](https://www.openpowerlifting.org/) dataset. 

---

## Project Overview

Ingestion and analysis of a large public dataset related to a personal hobby.

---

## Skills & Tools

- Python
- PostgreSQL
- SQL
- dbt Core
- Docker & Docker Compose
- Power BI

---

## Architecture

OpenPowerlifting CSV  
→ Python ingestion pipeline  
→ PostgreSQL (raw tables)  
→ dbt transformations  
→ Containerization
→ Power BI dashboards

---

## Data Ingestion

- Pulled data from the OpenPowerlifting CSV dataset using Python
- Loaded denormalized raw data into PostgreSQL
- Designed ingestion logic to be repeatable and isolated from business logic

This layer is responsible only for getting data into the database safely and consistently.

---

## Data Modeling with dbt

dbt Core is used to transform raw tables into an analytics-ready dimensional model.

**Model structure**
- Staging models to clean and standardize raw fields
- Fact tables for competition results and lifts
- Dimension table for lifters

---

## Containerized Analytics Stack

The project is fully containerized using Docker.

**Docker Compose services**
- PostgreSQL database
- Python data ingestion service
- dbt Core transformation service

This setup mirrors real-world analytics environments and ensures consistent local development.

---

## Power BI Dashboards

Power BI connects directly to the transformed fact and dimension tables.

### Lifter Performance Dashboard
- Individual lifter profiles
- Historical performance trends
- Best lifts across competitions

<img width="1916" height="1079" alt="Screenshot 2026-01-10 144241" src="https://github.com/user-attachments/assets/64d14c19-1db3-4463-9b05-560c921f9c17" />

### Weight Class Analysis
- Performance distribution by weight class
- Trend analysis across classes

<img width="1918" height="1079" alt="Screenshot 2026-01-10 142443" src="https://github.com/user-attachments/assets/8ad49925-c47c-43cc-a363-483ee7edc64c" />

---


