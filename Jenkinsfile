pipeline {
    agent {
        docker {
            image 'docker:stable' 
            args '-v /var/run/docker.sock:/var/run/docker.sock' 
        }
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20'))
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

