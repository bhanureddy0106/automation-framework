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

                bat 'dir'
            }
        }

        stage('Install Dependencies') {

            steps {

                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Clean Previous Reports') {

            steps {

                bat 'rmdir /s /q allure-results || exit 0'
                bat 'rmdir /s /q allure-report || exit 0'
            }
        }

        stage('Run Tests in Parallel') {

            steps {

                bat 'pytest tests -n 2 --html=reports/report.html --self-contained-html --alluredir=allure-results'
            }
        }

        stage('Archive Reports') {

            steps {

                archiveArtifacts artifacts: 'reports/*, screenshots/*, logs/*, allure-results/*', allowEmptyArchive: true
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

        stage('Publish Allure Report') {

            steps {

                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}