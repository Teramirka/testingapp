

pipeline {
    agent { label 'docker' }
    environment {
        FLASK_PORT = '5000'
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'master', url: 'https://github.com/Teramirka/testingapp.git'
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
                // Tests here
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image('blog_app').push('latest')
                    }
                    sh 'docker-compose down && docker-compose up -d'
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

