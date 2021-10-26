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
          sh 'python -m pytest -vv ./image_recognizer_app/test'
          sh 'mkdir -p dir1/reports/html'
          sh 'echo reports > dir1/reports/html/index.html'
          sh 'docker cp python-c-ut:dir1 .' 
      }
      post {
        always {
          archiveArtifacts 'dir1/reports/html'
        }
      }
    }
  }
}