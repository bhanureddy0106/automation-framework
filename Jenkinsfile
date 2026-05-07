pipeline {
    agent any

    stages {

        stage('Checkout Code from Git') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Start Selenium Grid (Docker)') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pytest -v --alluredir=reports/allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat 'allure generate reports/allure-results -o reports/allure-report --clean'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Execution Completed'
        }
    }
}