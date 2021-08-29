pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                echo "Starting build"
            }
        }
        stage('Test'){
            steps {
                echo "Starting test"
            }
        }
        stage('Deploy') {
            steps {
                echo "Starting deploy"
            }
        }
    }
}