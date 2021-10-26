pipeline {
  agent any
  environment {
    HOST_WORKSPACE = '${WORKSPACE}'
  }
  stages {
    stage('UnitTest') {
      agent {
        docker { 
          image 'tensorflow/tensorflow:2.6.0'
          args '-v ${HOST_WORKSPACE}:/tmp/reports --user jenkins'
          }
      }
      steps { 
          sh 'echo ${HOST_WORKSPACE}'
          sh 'pip install -r requirements.txt'
          sh 'python -m pytest -vv ./image_recognizer_app/test'
          sh 'ls -la /tmp/reports/'
          sh 'touch /tmp/reports/filereport'
      }
      // post {
      //   always {
      //     archiveArtifacts 'dir1/reports/html'
      //   }
      // }
    }
  }
}