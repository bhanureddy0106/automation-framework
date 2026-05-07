pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                git branch: 'main',
                url: 'https://github.com/bhanureddy0106/automation-framework.git'
            }
        }

        stage('Go To Project Folder') {
            steps {
                sh 'ls'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Clean Previous Reports') {
            steps {
                sh '''
                rm -rf allure-results reports
                mkdir -p reports
                '''
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                sh '''
                python3 -m pytest tests -n 2 \
                --dist loadscope \
                --cache-clear \
                --html=reports/report.html \
                --self-contained-html \
                --alluredir=allure-results
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*, screenshots/*, logs/*, allure-results/*',
                allowEmptyArchive: true
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])
            }
        }
    }
}