pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate') {
            steps {
                sh 'python3 --version'
                sh 'test -f app.py'
                sh 'test -f tests/test_app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
                sh '.venv/bin/python -m pytest -q'
            }
        }

        stage('Build') {
            steps {
                sh 'mkdir -p build'
                sh 'cp app.py build/app.py'
                sh 'test -s build/app.py'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    mkdir -p /tmp/lab1-deployment
                    cp build/app.py /tmp/lab1-deployment/app.py

                    pkill -f "[p]ython3 /tmp/lab1-deployment/app.py" || true

                    nohup python3 /tmp/lab1-deployment/app.py \
                      > /tmp/lab1-deployment/server.log 2>&1 &

                    sleep 2
                    curl --fail http://localhost:8081/
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
