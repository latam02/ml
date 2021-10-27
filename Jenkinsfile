pipeline {
  // options {
  //     timeout(time: 1, unit: 'HOURS') 
  // }
  // enviroments{
  //   SONAR_TOKEN = credentials('variable jenkins')
  // }
  agent any
  stages {
    stage('UnitTest') {
      agent {
        docker { 
          image 'crgv/tensorflow-c:2.6.0'
          }
      }
      steps {
          sh 'apt-get update -y' 
          sh 'pip install --upgrade pip'
          sh 'apt-get -y install ffmpeg libsm6 libxext6  -y'
          sh 'pip install -r requirements.txt --no-cache-dir'
          sh 'tail -f /dev/null'
          sh 'python -m pytest -vv ./image_recognizer_app/test/test_nasnet.py'
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