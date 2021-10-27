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
          image 'crgv/python-c:3.8.12'
          }
      }
      steps { 
          sh 'pip install -r requirements.txt --no-cache-dir'
          sh 'python -m pytest -vv ./image_recognizer_app/test/test_nasnet.py'
          sh 'python -m pytest --html=../../report.html -s'
          sh 'tail -f /dev/null'
      }
      post {
        always {
          archiveArtifacts artifacts: 'report.html', followSymlinks: false
        }
      }
    }
  }
}