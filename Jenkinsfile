pipeline {
    agent {
        docker {
            image 'docker:stable' 
            args '-v /var/run/docker.sock:/var/run/docker.sock' 
        }
    }
    environment {
        FLASK_PORT = '5000'
        DOCKERHUB = credentials('docker-hub-credentials')
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'master', url: 'https://github.com/Teramirka/testingapp.git'
                sh 'ls -al'
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker info' 
                    sh 'docker build -t blog_app -f app/Dockerfile app'
                }
            }
         }

        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                //  test commands here
            }
         }
    
        stage('Deploy') {
            steps {
                script { 
                    sh 'docker login -u $DOCKERHUB_USR -p $DOCKERHUB_PSW'
                    sh 'docker tag blog_app $DOCKERHUB_USR/blog_app:latest'
                    sh 'docker push $DOCKERHUB_USR/blog_app:latest'
                    try {
                        sh 'docker-compose down && docker-compose up -d'
                    } catch (Exception e) {
                        echo "Deployment failed: ${e.getMessage()}"
                    } finally {
                        echo "Deployment stage completed."
                    }
                }
            }
         }
      }
post {
        always {
            cleanWs()
        }
    }
}

