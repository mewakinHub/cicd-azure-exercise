# Exercise 2: Setting Up CI/CD Pipelines for Machine Learning Models

## Overview
In this exercise, you will learn how to set up a Continuous Integration and Continuous Deployment (CI/CD) pipeline using Azure DevOps, specifically tailored for deploying machine learning models on Google Cloud Platform (GCP).

## Tasks from Senior
- เริ่มจาก ci(**automation**), using Terraform for **infrastructure**
- gcp has it own version for deployment in enterprise

- monitoring ไว้จบแล้วค่อยมาดูว่าลองทำเล่นเลยมั้ย

## Full Detail ⛑️
For a more detailed understanding of the CI/CD concepts discussed here, please refer to the following documents in the `ex2-docs` directory:
- [CI/CD Roadmap & learning resource](./ex2-docs/learning-resource.md)

## Objectives
- Create a CI pipeline in Azure DevOps.
- Build Docker images for machine learning deployment.
- Use Terraform to deploy resources on GCP.
- Integrate monitoring and logging for deployments.

## Instructions

### Step 1: Azure DevOps Setup
1. Create a new pipeline in Azure DevOps using the Azure Repos Git repository.
2. Define the pipeline configuration in a `azure-pipeline.yml` file. This file will automate testing, building Docker images, and pushing them to GCP's Artifact Registry.

### Step 2: Docker Image for ML Model
1. Create a `Dockerfile` in the root of your project that specifies the environment and dependencies for your machine learning model.
2. Configure the Azure Pipeline to build and push this Docker image to GCP's Artifact Registry using the following steps in your YAML file:
   ```yaml
   - script: |
       docker build -t gcr.io/$(GCP_PROJECT_ID)/my-model:$(Build.BuildId) .
       docker push gcr.io/$(GCP_PROJECT_ID)/my-model:$(Build.BuildId)
     displayName: 'Build and Push Docker Image'
   ```

### Step 3: Deploy Using Terraform
1. Write Terraform scripts to define the required infrastructure on GCP, including Compute Engine instances or Cloud Run services.
2. Add Terraform steps to your Azure Pipeline to deploy or update infrastructure:
   ```yaml
   - script: |
       terraform init
       terraform apply -auto-approve
     displayName: 'Deploy with Terraform'
   ```

### Step 4: Monitoring and Logging
1. Set up Google Stackdriver for monitoring the performance of your deployed models.
2. Integrate alerts within Azure DevOps to notify you of any deployment issues or performance degradation.


## Conclusion
Upon completion of this exercise, you will have a fully functional CI/CD pipeline that deploys a machine learning model to GCP, with monitoring and logging configured to track the application's health and performance.