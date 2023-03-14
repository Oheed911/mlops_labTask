pipeline {
  agent any
  
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t myflaskapp .'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run myflaskapp python test.py'
      }
    }
    stage('Deploy') {
      steps {

        sh 'docker run -d -p 5000:5000 myflaskapp'
      }
    }
    stage('Expose') {
      steps {
        ngrok([httpPort: 5000])
    }
    }
}
}