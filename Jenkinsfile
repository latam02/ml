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
          image 'crgv/tensorflow-c:2.6.2'
          }
      }
      steps {
          
          sh 'pip install --upgrade pip'
          sh 'pip install -r requirements.txt --no-cache-dir'
          sh 'python -m pytest --html=report.html -s'
      }
      post {
        always {
          archiveArtifacts artifacts: '**/*.html', followSymlinks: false
        }
      }
    }
  }
}