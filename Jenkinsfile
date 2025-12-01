pipeline {
    agent { 
        label 'main'
    }
    tools {
        maven 'Maven_3_8_4'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout code from SCM
            }
        }
        stage('Build') {
            steps {
                sh 'echo Hello from Jenkins!'
            }
        }
        stage('Test') {
            steps {
                sh 'And this is a test stage'
            }
        }
    }
}

