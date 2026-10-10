# Lab 1: DevOps Foundations & Continuous Integration

**Name:** Amit  
**Roll Number:** 2301010471  
**Operating System:** Ubuntu Linux 24.04 LTS

---

## 1. Objective

To establish a basic DevOps workflow using Git, GitHub, and Jenkins. This lab demonstrates version control, continuous integration, automated testing, build automation, and application deployment through a Jenkins CI/CD pipeline.

## 2. Tools and Technologies

- Ubuntu Linux 24.04 LTS
- Git
- GitHub
- Jenkins
- Python 3
- pytest
- Visual Studio Code

## 3. Project Structure

    lab1-devops-ci-cd/
    ├── app.py
    ├── tests/
    │   └── test_app.py
    ├── requirements.txt
    ├── .gitignore
    ├── Jenkinsfile
    ├── README.md
    └── evidence/
        ├── 01-ubuntu-tools.png
        ├── 02-github-repository.png
        ├── 03-git-commits.png
        ├── 04-jenkins-build.png
        ├── 05-console-success.png
        ├── 06-pipeline-stages.png
        └── 07-deployed-app.png

## 4. Application Overview

The project contains a simple Python HTTP server that returns a message confirming that the application is running.

### Run the Application

    python3 app.py

### Verify the Application

    curl http://localhost:8081/

Expected response:

    Lab 1 CI/CD deployment is working!

## 5. Jenkins CI/CD Pipeline

The pipeline is defined in the Jenkinsfile and consists of five stages.

### Stage 1: Checkout

Retrieves the application source code from the GitHub repository.

### Stage 2: Validate

Checks the Python environment and verifies that the required project files exist.

### Stage 3: Test

Installs the required dependencies and executes automated tests using pytest.

### Stage 4: Build

Creates a deployable copy of the application.

### Stage 5: Deploy

Starts the application and verifies its response using curl.

**Jenkins URL:** http://localhost:8080  
**Application URL:** http://localhost:8081

## 6. Git Commands Used

### Initialize the Repository

    git init

### Stage Project Files

    git add .

### Commit Changes

    git commit -m "feat: add sample app and Jenkins pipeline"

### Rename the Branch

    git branch -M main

### Connect the GitHub Repository

    git remote add origin https://github.com/YOUR-USERNAME/lab1-devops-ci-cd.git

### Push the Code to GitHub

    git push -u origin main

## 7. Execution and Verification

The project is verified through the following steps:

1. Configure Git for version control.
2. Upload the application source code and Jenkinsfile to GitHub.
3. Configure Jenkins to retrieve the repository.
4. Execute the Jenkins CI/CD pipeline.
5. Review the Jenkins build status and console output.
6. Verify the application using an HTTP request.
7. Capture screenshots and store them in the evidence directory.

## 8. Results

- Git was configured for source code management.
- Application source code and Jenkins pipeline configuration were stored in GitHub.
- Jenkins was configured to execute the defined pipeline stages.
- Automated testing was configured using pytest.
- The Python application was tested through an HTTP request.
- Screenshots were collected as evidence of the experiment.

Note: The final results should reflect the stages that actually completed successfully in Jenkins.

## 9. Conclusion

This lab demonstrates the fundamentals of DevOps by integrating Git-based version control with Jenkins CI/CD automation. It provides practical experience in source code management, automated testing, build automation, application deployment, and project documentation.

## 10. Evidence

The evidence directory should contain actual screenshots of:

- Ubuntu version and installed tool versions.
- GitHub repository and project files.
- Git commit history.
- Successful Jenkins build.
- Jenkins pipeline stages.
- Jenkins console output.
- Running application on port 8081.

## 11. Repository Link

**GitHub Repository:**  
https://github.com/YOUR-USERNAME/lab1-devops-ci-cd

---

**Submitted by:** Amit  
**Roll Number:** 2301010471
