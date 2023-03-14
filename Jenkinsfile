pipeline {
  agent any
  
  stages {
    stage('Build') {
      steps {
        script {
          def app = docker.build('myflaskapp', '-f Dockerfile .')
        }
      }
    }
    stage('Test') {
      steps {
        sh 'docker run myflaskapp python test.py'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker stop myflaskapp || true'
        sh 'docker rm myflaskapp || true'
        sh 'docker run -d --name myflaskapp -p 5000:5000 myflaskapp'
      }
    }
    stage('Expose') {
      steps {
        ngrok([httpPort: 5000])
      }
    }
  }
}
