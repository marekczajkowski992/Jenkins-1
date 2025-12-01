pipeline {
    agent any
    tools {
        maven 'Maven_3_9_11'
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

