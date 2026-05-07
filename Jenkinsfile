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
                dir('C:\\Users\\Bhanu\\Desktop\\Automation Framework Architecture') {
                    bat 'dir'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('C:\\Users\\Bhanu\\Desktop\\Automation Framework Architecture') {
                    bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                }
            }
        }

        stage('Clean Previous Reports') {
            steps {
                dir('C:\\Users\\Bhanu\\Desktop\\Automation Framework Architecture') {
                    bat '''
                        if exist allure-results rmdir /s /q allure-results
                        if exist reports rmdir /s /q reports
                        mkdir reports
                    '''
                }
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                dir('C:\\Users\\Bhanu\\Desktop\\Automation Framework Architecture') {
                    bat '''
                        venv\\Scripts\\python.exe -m pytest tests -n 2 ^
                        --dist loadscope ^
                        --cache-clear ^
                        --html=reports\\report.html ^
                        --self-contained-html ^
                        --alluredir=allure-results
                    '''
                }
            }
        }

        stage('Archive Reports') {
            steps {
                dir('C:\\Users\\Bhanu\\Desktop\\Automation Framework Architecture') {
                    archiveArtifacts artifacts: 'reports/*, screenshots/*, logs/*, allure-results/*', allowEmptyArchive: true
                }
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