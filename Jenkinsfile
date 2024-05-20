pipeline {
    agent {
        docker {
            image 'docker:stable' 
            args '-v /var/run/docker.sock:/var/run/docker.sock' 
        }
    }
    environment {
        FLASK_PORT = '5000'
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
    
        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'docker-hub-credentialsPassword', usernameVariable: 'docker-hub-credentialsUser')]) {
                  sh "docker login -u ${env.docker-hub-credentialsUser} -p ${env.docker-hub-credentialsPassword}"
                  sh 'docker push teramir/spring-petclinic:latest'
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
