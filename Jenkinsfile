pipeline {
    agent {
        docker {
            image 'docker:stable' 
            args '-v /var/run/docker.sock:/var/run/docker.sock' 
        }
    }
    environment {
        FLASK_PORT = '5000'
        DOCKERHUB_CREDENTIALS=credentials('docker-hub-credentials')
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
                    sh 'docker build -t teramir/blog_app:latest ./app/'
                }
            }
         }

        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                //  test commands here
            }
         }

        stage('Login') {
            steps {
                sh echo '$DOCKERHUB_CREDENTIALS'
                sh 'echo $DOCKERHUB_CREDENTIALS | docker login -u $DOCKERHUB_CREDENTIALS --password-stdin'
            }
        
         }
    
        stage('Deploy') {
            steps {
                sh 'docker push teramir/blog_app:latest'
                sh 'docker-compose version' 
                sh 'docker-compose down && docker-compose up -d'
                }
            }
         }
    }
    post {
        always {
            sh 'docker logout'
            cleanWs()
        }
    }
