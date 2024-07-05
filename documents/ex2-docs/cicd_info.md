### Autometic(Programatically) vs Manual
To ensure consistency and reliability, it's generally better to automate the creation of resources like repositories and images within your CI/CD pipeline. Automating these steps ensures that the necessary resources exist every time the pipeline runs, reducing the risk of manual errors and making the deployment process more seamless.

### Existing Information
**GCP Project ID**: `cpf-aiml-innovation` <br />
**Service Account Email**: `aiml-workflow-innovation@cpf-aiml-innovation.iam.gserviceaccount.com` <br />
**Azure DevOps Repo**: `https://dev.azure.com/DM-Data-Platform/AIML_Demo/_git/Mew2` <br />
**Azure DevOps Branch**: `feature/cicd` (also have branch `main`) <br />
**GCP Artifact Registry Repository**: `asia-southeast1/intern-mew2-exercise` <br />
**Docker Image Name**: `intern-mew2-exercise/stock-indicator-service` <br />
**Cloud Run Service Name**: `stock-indicator-service` <br />
**Azure Devops service connection(which connected to GCP via JSON key)**: `aiml-workflow-innovation` (use for auth and perform action in CD)

**GCP Console Links**:
  - **Artifact Registry**: https://console.cloud.google.com/artifacts/docker/cpf-aiml-innovation/asia-southeast1/intern-mew2-exercise?hl=th&project=cpf-aiml-innovation
  - **Cloud Run**: https://console.cloud.google.com/run?hl=th&project=cpf-aiml-innovation

**Service Account:** (`SERVICE_ACCOUNT_EMAIL: 'aiml-workflow-innovation@cpf-aiml-innovation.iam.gserviceaccount.com'`)
- A service account in Google Cloud is a special type of Google account that belongs to your application or a virtual machine (VM), instead of to an individual end user.
- Service accounts are used to make authorized API calls and to authenticate to Google Cloud services.
- Service accounts can have IAM roles assigned to them, granting them permissions to perform specific actions on Google Cloud resources.

**JSON Key File:** (`JSON_KEY_FILE: 'cpf-aiml-innovation-61af10fd34f9.json'`)
- A JSON key file is a private key file associated with a service account. It contains credentials that allow applications and users to authenticate as the service account.
- The JSON key file is downloaded when creating a service account key in the Google Cloud Console. This key file is used to authenticate and authorize actions performed by the service account.

**example of how to use this service acc key pair**
However, in your pipeline, the JSON key file already contains all the necessary information for authentication, including the service account email. The gcloud auth activate-service-account command uses the JSON key file to authenticate, so explicitly specifying the service account email is not required there.
```
- script: |
    export GOOGLE_APPLICATION_CREDENTIALS=$(downloadJsonKey.secureFilePath)
    gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
    gcloud config set project $(GCP_PROJECT_ID)
  displayName: 'Authenticate with GCP and Verify Permissions'
```

# Monitor result Step

1. **Commit and Push Changes**:
    - Commit the `azure-pipelines-cd.yml` and any other changes to your repository.
    - Push the changes to trigger the pipeline.

2. **Monitor Pipeline Execution**:
    - Go to Azure DevOps Pipelines and monitor the pipeline execution to ensure all stages complete successfully.

3. **Verify Deployment and Service**:
    - Go to the Cloud Run section in GCP and verify that the service is running.
    - Use Postman or curl to test the deployed service.

POST method w/ URL on specific endpoint: `https://mew2-service-nolntqmyrq-as.a.run.app/api/v1/stock-data`
body JSON raw:
```
{
    "symbol": "AAPL",
    "indicator": "RSI"
}
```

### Deployment on Cloud run

**Deploy to Cloud Run:** 🚢
   - Containerize your application using Docker. (GCP has it own version of dockerhub ofr enterprise uses <-- I'll publish to it with my CI pipeline)
   - Push Docker images to GCP’s Artifact Registry.
   - Deploy to Cloud Run using Terraform for infrastructure provisioning. (use IaC tools to spinup cloud resources) 

Yes, deploying your application to Google Cloud Run is akin to running your server in the cloud. Cloud Run is a managed platform that automatically scales your application based on incoming requests, and it can scale down to zero when not in use. Here’s how it manages costs and operations:

1. **Autoscaling to Zero**: Cloud Run can automatically scale down your services to zero instances when no requests are coming in. This means you're not charged for the compute resources when your service isn't being used.

2. **Billing Based on Use**: You are billed for the actual compute time your service consumes, measured to the nearest 100 milliseconds. This makes it a cost-effective option because you only pay when your service is actively handling requests.

### Managing and Monitoring Services

To see what services are running and manage them:

1. **Google Cloud Console**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to the "Cloud Run" section under the compute services.
   - Here, you will see a list of all your services. You can view their status (whether they are actively handling requests), and other details like the number of instances currently running.

2. **Stopping or Deleting Services**:
   - If you need to stop a service temporarily or delete it to avoid incurring charges, you can do this from the Cloud Run interface in the Google Cloud Console.
   - To stop a service, you can disable it. Disabling the service prevents it from serving any more requests but retains its configuration and data so you can re-enable it later.
   - To delete a service, simply select the service in the Cloud Run dashboard and use the delete option. This removes the service completely and you will not incur further charges for it.

3. **Setting Budget Alerts**:
   - To prevent unexpected costs, you can set budget alerts in Google Cloud Billing. This allows you to receive notifications if your spending exceeds the threshold you set. It's a good way to keep tabs on costs without having to check manually.

4. **Logging and Monitoring**:
   - Google Cloud provides logging and monitoring through Cloud Logging and Cloud Monitoring, allowing you to see detailed logs of what your service is doing and monitor metrics like request counts, latency, etc. This can help in understanding the usage patterns and operational health of your services.

By using these tools and features, you can manage your services on Cloud Run efficiently, ensuring that you maintain control over costs and operations.
