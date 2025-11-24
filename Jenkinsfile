// Jenkinsfile

pipeline {
    agent any

    // ⚠️ CUSTOMIZE THESE ENVIRONMENT VARIABLES! ⚠️
    environment {
        // 1. ID of your DockerHub credentials in Jenkins (MUST MATCH the ID you set up)
        DOCKERHUB_CRED = 'your-dockerhub-creds-id'
        
        // 2. Change 'yourusername/myapp' to your actual DockerHub username and desired repository name
        IMAGE_NAME = 'pavanrajnikam/pavan-jenkins-app' 
        
        // 3. Automatically tags the image with the Jenkins build number (e.g., v1.1, v1.2)
        IMAGE_TAG = "v1.${BUILD_NUMBER}" 
        
        // 4. Update with your actual repository URL and branch
        GIT_BRANCH = 'master' 
        GIT_URL = 'https://github.com/Pavan-rajn/Jenkins.git' 
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning repository from ${env.GIT_URL} branch ${env.GIT_BRANCH}"
                git branch: env.GIT_BRANCH, url: env.GIT_URL
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building image ${env.IMAGE_NAME}:${env.IMAGE_TAG}"
                // The --build-arg passes the IMAGE_TAG into the Dockerfile for logging/versioning
                sh "docker build --build-arg IMAGE_TAG=${env.IMAGE_TAG} -t ${env.IMAGE_NAME}:${env.IMAGE_TAG} ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CRED,
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh "echo \$PASS | docker login -u \$USER --password-stdin"
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                sh "docker push ${env.IMAGE_NAME}:${env.IMAGE_TAG}"
            }
        }

        stage('Logout Docker') {
            steps {
                sh "docker logout"
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        success {
            echo "✅ Docker image pushed successfully: ${env.IMAGE_NAME}:${env.IMAGE_TAG}"
            // Run the image locally to confirm it works
            echo "To run your image locally, use: docker run --rm ${env.IMAGE_NAME}:${env.IMAGE_TAG}"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}
