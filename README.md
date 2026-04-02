# Support Vector Machine Performance Monitoring

## Project Overview

This project demonstrates a complete ML monitoring pipeline using Support Vector Machine (SVM) for predictive modeling, with comprehensive performance tracking and visualization.

## Technologies Used

- Python
- Flask
- SciKitLearn
- Grafana
- Prometheus
- Docker
- cAdvisor
- Pandas
- Kubernetes

## Successes

- **Developed a Dockerized Flask API** to serve a Support Vector Machine classifier for predictive modeling.
- **Tested performance and resource utilization** on both 2000 and 8000 samples.
- **Integrated Prometheus metrics** for storage of CPU, memory, and stage-wise latency (tuning, training, inference) and time-series graphing.
- **Created Grafana dashboards** for real-time visualization of resource consumption and latency metrics, enabling monitoring of ML service performance.
- **Collaborated with DevOps workflow** by containerizing the service, ensuring reproducible deployments and scalable testing.

## Challenges

- **Debugging containerized environment metrics collection.** Verified container labels and Prometheus targets, adjusting PromQL queries for CPU, memory, and latency metrics to ensure correct visualization. Also exposed endpoints during training of the model for easier data scraping.

## Project Structure

```
SVM-monitoring/
├── SVM-Monitoring/
│   ├── Dockerfile
│   ├── main.py
│   ├── svm/
│   │   ├── requirements.txt
│   │   └── svm_classifier.py
│   └── k8s/
│       ├── cAdvisor/
│       ├── grafana/
│       ├── prometheus/
│       └── svm/
└── README.md
```

## Getting Started

### Prerequisites

- Docker
- Kubernetes (for full deployment)
- Python 3.8+ (for local development)

### Local Development

1. Clone the repository
2. Navigate to the SVM-Monitoring directory
3. Install dependencies:
   ```bash
   cd svm
   pip install -r requirements.txt
   ```
4. Run the SVM classifier:
   ```bash
   python svm_classifier.py
   ```
5. Test the API:
   ```bash
   python ../main.py
   ```

### Docker Deployment

1. Navigate to the SVM-Monitoring directory
2. Build the Docker image:
   ```bash
   docker build -t svm-classifier .
   ```
3. Run the container:
   ```bash
   docker run -p 5002:5002 svm-classifier
   ```

### Kubernetes Deployment

Deploy the full monitoring stack using the Kubernetes manifests in the `SVM-Monitoring/k8s/` directory.

## Usage

The Flask API exposes:
- `/api/classify` - POST endpoint for SVM classification
- `/metrics` - GET endpoint for Prometheus metrics

## Monitoring

- Prometheus collects metrics on CPU, memory, and latency
- Grafana provides dashboards for visualization
- cAdvisor monitors container resource usage
