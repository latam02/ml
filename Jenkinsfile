pipeline {
  agent any
  stages {
    stage('UnitTest') {
      agent {
        docker { 
          image 'python:3.8.12'
          }
      }
      steps { 
          sh 'pip install -r requirements.txt --no-cache-dir'
          sh 'python -m pytest -vv ./image_recognizer_app/test/'
          sh 'echo new > report.html'
          sh 'ls -la'
      }
      post {
        always {
          archiveArtifacts artifacts: '**/*.html', followSymlinks: false
        }
      }
    }
  }
}