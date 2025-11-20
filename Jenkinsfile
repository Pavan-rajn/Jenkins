pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Pavan-rajn/Jenkins.git',branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo "Building application..."
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
            }
        }
    }
}
