# Weather Data Ingestion with AWS Lambda

---

## Project Description

This project is a **data ingestion pipeline** that fetches weather data using an **AWS Lambda function** and stores it in an **S3 bucket**. The function is triggered **every hour** using **Amazon EventBridge**. The **Lambda function is written in Python** and uses the `requests` library to interact with the weather API.

To automate the infrastructure setup, **Infrastructure-as-Code (IaC)** has been implemented using **AWS CloudFormation** and stored as a YAML file. Additionally, **IAM roles and policies** have been defined to grant Lambda access to **S3 and CloudWatch Logs**.

---

## Source APIs

1. **[Weather Data API](https://openweathermap.org/current)** – The source API for fetching weather data (Call current weather data).  
2. **[Geocoding API](https://openweathermap.org/api/geocoding-api#direct)** – Used to generate the geolocation of the city (extract latitude and longitude).  

---

## Implementation Details

- **AWS Services Used**:
  - **Lambda** – Runs the Python script to fetch and store data.
  - **S3** – Stores the ingested data.
  - **EventBridge** – Triggers Lambda every hour.
  - **IAM** – Manages permissions for Lambda.
  - **CloudFormation** – Defines infrastructure as code.
  - **CloudWatch** – Monitors logs and execution performance.

---

## Assumptions

- The `requests` library has been included in the Lambda function.
- The API provides hourly updates, so the function is triggered at the same frequency.
- The IAM permissions allow Lambda to **write to S3** and **log to CloudWatch**.

