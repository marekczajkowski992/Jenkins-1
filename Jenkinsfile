pipeline {
    agent { 
        label 'main'
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
                sh 'echo And this is a test stage'
            }
        }
    }
}

