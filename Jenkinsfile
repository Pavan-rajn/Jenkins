pipeline {
    agent any

    environment {
        VERSION = "2.0"
    }

    parameters {
        choice(name: 'ENV', choices: ['dev', 'qa', 'prod'], description: 'Select environment')
    }

    stages {
        stage('Build') {
            steps {
                echo "Building version ${VERSION}"
            }
        }

        stage('Test') {
            parallel {
                stage('Unit Tests') {
                    steps { echo "Running unit tests" }
                }
                stage('Integration Tests') {
                    steps { echo "Running integration tests" }
                }
            }
        }

        stage('Deploy') {
            when {
                expression { params.ENV == 'prod' }
            }
            steps {
                echo "Deploying to production"
            }
        }
    }

    post {
        always {
            echo "Pipeline completed"
        }
    }
}
