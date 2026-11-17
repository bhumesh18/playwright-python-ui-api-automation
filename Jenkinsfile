
pipeline {

    agent any

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    stages {

        // Stage 1: Get code from GitHub
        stage('Checkout') {
            steps {
                checkout scm

                bat 'git --version'
                bat 'python --version'
            }
        }

        // Stage 2: Prepare Python environment
        stage('Setup Python Environment') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat 'if not exist logs mkdir logs'
                bat 'if not exist test-results mkdir test-results'

                bat 'python -m venv .venv'

                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'

                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        // Stage 3: Install Playwright browser
        stage('Install Playwright Chromium') {
            steps {
                bat '.venv\\Scripts\\python.exe -m playwright install chromium'
            }
        }

        // Stage 4: Execute UI tests
        stage('UI Automation Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v ui_tests/ --html=reports/ui-report.html --self-contained-html --junitxml=reports/ui-junit.xml'
            }
        }

        // Stage 5: Execute API tests
        stage('API Automation Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v api_tests/ --html=reports/api-report.html --self-contained-html --junitxml=reports/api-junit.xml'
            }
        }
    }

    // Publish results even when a test stage fails
    post {

        always {

            junit(
                testResults: 'reports/*-junit.xml',
                allowEmptyResults: true
            )

            archiveArtifacts(
                artifacts: 'reports/*.html, reports/*-junit.xml, test-results/**, logs/*.log',
                allowEmptyArchive: true
            )
        }
    }
}
