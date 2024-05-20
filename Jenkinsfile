pipeline {
    agent {
        docker {
            image 'docker:stable' 
            args '-v /var/run/docker.sock:/var/run/docker.sock' 
        }
    }
    environment {
        FLASK_PORT = '5000'
        registry = "teramir/app_blog" 
        registryCredential = 'docker-hub-credentials' 
        dockerImage = '' 
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
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
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
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                }
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
