pipeline {
  agent any
  stages {
    stage('UnitTest') {
      agent {
      //   docker { 
      //     image 'tensorflow/tensorflow:2.6.0'
      //     args '--name python-c-ut'
      //     }
      // }
      steps {   
          
          sh 'pip install -r requirements.txt'
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