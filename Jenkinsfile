pipeline {
    agent {
        docker { image 'python:3.9-slim' }
    }
    environment {
        FLASK_PORT = '5000'
    }
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/Teramirka/testingapp.git'
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
                // Здесь вы можете добавить команды для запуска тестов
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
