# Stock Indicator Microservice

## Overview
This repository contains a FastAPI microservice designed to fetch daily stock prices from TradingView and compute technical indicators. It's built with a focus on clean coding practices, DDD principles, and extensibility.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Local Development](#local-development)
- [Docker Configuration](#docker-configuration)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Setup and Usage](#setup-and-usage)
- [Testing](#testing)
- [Azure Repo challenge](#Azure-Repo-challenge)

## Features
- **FastAPI Framework**: Utilizes FastAPI for efficient API development.
- **Technical Indicators**: Supports multiple indicators like SMA, EMA, and RSI.
- **Extensible Design**: Easily integrate additional stock APIs or indicators.
- **Error Handling and Logging**: Implements comprehensive error management and logging for robustness and troubleshooting.

## Architecture
The application employs Domain-Driven Design to ensure clean and maintainable code, structured into several directories each serving distinct roles:
- **`/app`**: Core application including business logic and API endpoints.
- **`/logs`**: For logging outputs, excluded from GitHub for security.

## Local Development
- [Development Instructions](#local-development)

## Docker Configuration
- [Docker Setup](Dockerfile)

## Project Structure
- **[app/](app/README.md)**: Application source code including models, services, API routes, and configurations.
- **[tests/](app/tests/README.md)**: Testing modules for unit and integration tests.

## Technologies
- FastAPI, Pytest, Docker, TradingView API, Pydantic(OOP concepts)

## Documentation
For more detailed information on development practices, setup, testing, and deployment, please refer to the [Documentation Folder](docs/).

- [Project Structure Overview](docs/structure.md)
- [Developer Guidelines](docs/developer.md) ❌
- [Environment Setup](docs/venv.md) Done ✅
- [Project Setup](docs/setup.md) ❌
- [Testing Procedures](docs/testing.md) ❌
- [Deployment Guidelines](docs/deployment.md) ❌

**Structure of the Documentation Folder**
```
/docs
│
├── structure.md           # Project Structure Overview
├── developer.md           # General guidelines for developers 
├── venv.md                # Virtual environment setup instructions.
├── setup.md               # Project setup and installation instructions.
├── testing.md             # Testing procedures and examples.(e.g., Dependency Injection)
└── deployment.md          # Deployment guidelines, including Docker usage.
```

## Setup and Usage
Detailed instructions on setting up the project and getting it running locally or via Docker.
### set up
Build image:
```
docker build -t mewakin/stock-indicator-service:latest .
```
run container:
```
docker run -p 8000:8000 mewakin/stock-indicator-service:latest
```
### usage
Make POST requests to `/api/v1/stock-data` with JSON payload specifying `symbol` and `indicator`.

## Testing
Guidelines on how to run tests using Pytest for unit, service, and API level.

To run these tests, you'll typically use a command-line tool like `pytest`. First, ensure you have `pytest` installed:

```bash
pip install pytest
```

Then, navigate to the root of your project and run:

```bash
pytest
```

This command will automatically find all files named `test_*.py` or `*_test.py` in your project and execute the defined test functions.

If you want to run tests in a specific file only, you can specify the file path:

```bash
pytest tests/test_api.py
```

For more advanced usage, such as running tests with coverage, you might use:

```bash
pip install pytest-cov
pytest --cov=app tests/
```

---
### Postman Request
<!-- print("RSI:", analysis.indicators.get("RSI"))
print("EMA10:", analysis.indicators.get("EMA10"))
print("SMA20:", analysis.indicators.get("SMA20")) -->

### using POSTMAN
1. POST -> http://localhost:8000/api/v1/stock-data w/ JSON BODY
```
{
    "symbol": "AAPL",
    "indicator": "RSI"
}
```

---
## Azure-Repo-challenge

### Introduction
- Overview of the project and its goals.
- Introduction to the tools used: Azure DevOps, Git, Docker.

### Challenges
1. **Branch Management Confusion**:
   - Difficulty in understanding and managing branches within Azure DevOps.
   - Issues with linking local branches to remote branches correctly.

2. **Merge Conflicts**:
   - Encountered merge conflicts due to differing histories and changes in Dockerfiles and other project files.
   - Struggled with resolving conflicts due to unfamiliarity with Git's merging mechanics.

3. **Remote Repository Issues**:
   - Problems arose from creating a new remote repository which led to unlinked histories.
   - Challenges in syncing local changes with the remote repository and vice versa.

### Solutions
1. **Git Branch Management**:
   - Learned to check out and switch branches effectively using Git commands.
   - Utilized Git's capabilities to rename and delete branches to manage the project structure better.

2. **Handling Merge Conflicts**:
   - Used Git commands to identify and resolve merge conflicts.
   - Adopted a systematic approach to reviewing changes between different branch states and deciding which changes to keep.

3. **Correcting Remote Repository Setups**:
   - Reinitialized the local repository to correctly link with the remote repository.
   - Practiced pushing and pulling from the remote repository to ensure all histories were aligned.

### Learnings from Senior Consultations
- Gained insights on the importance of proper branch management to avoid conflicts and ensure a smooth workflow.
- Learned best practices for using Git in a collaborative environment, such as always syncing with the remote before starting new work.

### CI/CD Introduction (Pending Learning)
- Preparing to delve into Continuous Integration/Continuous Deployment to automate the testing and deployment phases.

### Conclusion
- Reflect on the journey of overcoming initial hurdles with version control and deployment tools.
- Outline the next steps in learning and implementing CI/CD within the project.

### Appendices
- Include logs of commands used, errors encountered, and screenshots of critical steps or errors.

