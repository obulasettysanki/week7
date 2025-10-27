pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t mypythonflaskapp SamplePythonFlaskApp"
            }
        }
        stage('Run') {
            steps {
                echo "Running container..."
                sh "docker rm -f mycontainer || true"
                sh "docker run -d -p 5050:5000 --name mycontainer mypythonflaskapp"
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}