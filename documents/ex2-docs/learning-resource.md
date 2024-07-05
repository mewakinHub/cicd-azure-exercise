To effectively learn and implement CI/CD using the project stock microservice, you can follow a structured roadmap utilizing the resources provided by your senior. Here’s a detailed plan to get you started:

### Roadmap to Learn CI/CD

#### 1. Understand the Fundamentals of CI/CD
- **Resource:** Video
- [The IDEAL & Practical CI/CD Pipeline - Concepts Overview](https://youtu.be/OPwU3UWCxhw?si=TIo-yya0aIt4Z9XG)
- [The REVISED CI / CD Pipeline - Making Improvements](https://youtu.be/OcaUQrRo7-Q?si=I8V2q5zkzlIs3Wki)
- **Action:** Watch the video to understand the basic concepts of CI/CD, including source control, build processes, testing environments, and deployment strategies.
- [CI/CD Pipeline](technical-knowledge/pipeline.md)

#### 2. Hands-on Practice with CI
- **Resource:** Azure Pipelines Documentation
- **Action:** Start with the basics of CI using Azure Pipelines. Follow tutorials to set up a basic CI pipeline, focusing on configuring builds, running unit tests, and ensuring code coverage.
  - **Link:** [Azure Pipelines Documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops)

#### 3. Learn Infrastructure as Code (IaC)
- **Resource:** Terraform Documentation and Tutorials
- **Action:** Study the basics of Terraform to understand how to spin up cloud resources using IaC tools. This knowledge is crucial for automating the provisioning of infrastructure required for your CI/CD pipeline.

#### 4. Containerization and Deployment
- **Resource:** GCP Artifact Registry and Cloud Run
- **Action:** Learn how to containerize your applications using Docker(Docker image) and publish them to GCP’s Artifact Registry. Then, deploy these containers on Cloud Run using your CI/CD pipeline.
  - **Key Points:**
    - **Docker:** Understand the basics of Docker and how to create Docker images.
    - **Artifact Registry:** Learn how to push Docker images to GCP’s Artifact Registry.
    - **Cloud Run:** Get familiar with deploying and managing containerized applications on Cloud Run.

#### 5. Implementing a Complete CI/CD Pipeline
- **Resource:** Practical Implementation on AWS and Azure
- **Action:** Follow along with practical guides and tutorials to implement a complete CI/CD pipeline using AWS and Azure services.
  - **Link:** AWS Learning Accelerator and CodePipeline Tutorial
    - **AWS CodePipeline:** Learn how to set up pipelines for building, testing, and deploying code.
    - **Azure Pipelines:** Extend your knowledge from step 2 to include continuous delivery and deployment.

#### 6. Monitoring and Rollbacks
- **Resource:** Advanced CI/CD Concepts (Video)
- **Action:** Watch the video’s sections on monitoring and rollbacks to understand how to set up monitoring for your production environment and configure automatic rollbacks.
  - **Key Points:**
    - **Monitoring:** Learn how to set up alarms and monitoring systems to detect issues in production.
    - **Rollbacks:** Understand how to configure automatic rollbacks to ensure quick recovery from failures.

### Project Implementation Plan

1. **Set Up Source Control:**
   - Use Azure Repo(is this also called Git?) for version control.
   - Ensure pull request reviews are in place.

2. **Configure the Build Process:**
   - Compile code and dependencies.
   - Run unit tests and ensure high code coverage.

3. **Set Up Testing Environment:**
   - Configure integration tests to validate interactions between different parts of the application.

4. **Deploy to Cloud Run:** 🚢
   - Containerize your application using Docker. (GCP has it own version of dockerhub ofr enterprise uses <-- I'll publish to it with my CI pipeline)
   - Push Docker images to GCP’s Artifact Registry.
   - Deploy to Cloud Run using Terraform for infrastructure provisioning. (use IaC tools to spinup cloud resources) 

5. **Monitoring and Rollback:**
   - Set up monitoring tools to track production performance.
   - Configure automatic rollbacks for error detection and resolution.

6. **Continuous Improvement:**
   - Regularly review and improve your CI/CD pipeline based on feedback and performance metrics.

### Additional Resources

- **Recommended Books:**
  - Clean Code
  - Clean Architecture
  - Head First Design Patterns
  - Domain-Driven Design
  - Code Complete
  - The Pragmatic Programmer
  - Algorithms
  - Working Effectively with Legacy Code
  - Refactoring