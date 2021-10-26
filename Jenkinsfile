pipeline {
  options {
      timeout(time: 1, unit: 'HOURS') 
  }
  agent any
  stages {
    stage('UnitTest') {
      agent {
        docker { 
          image 'crgv/python-c:3.8.12'
          }
      }
      steps { 
          sh 'pip install --upgrade pip'
          sh 'pip install -r requirements.txt --no-cache-dir'
          sh 'python -m pytest -vv --cov=app ./image_recognizer_app/test/'
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