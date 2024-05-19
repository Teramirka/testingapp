pipeline {
    agent {
        docker { image 'python:3.9-slim' }
    }
    environment {
        FLASK_PORT = '8000'
    }
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/Teramirka/testingapp'
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('blog_app', '-f app/Dockerfile app')
                }
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                // Here we put our tests I currently don't have
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_credentials') {
                        docker.image('blog_app').push('latest')
                    }
                    docker-compose.down()
                    docker-compose.up('-d')
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
