pipeline {
  agent any
  environment{
    SONAR_TOKEN = credentials('sonar_token')
  }
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
    stage("CodeQuality") {
      steps {
          withSonarQubeEnv('sonarqube') {
              sh '/var/jenkins_home/sonar-scanner-4.4.0.2170-linux/bin/sonar-scanner -Dsonar.organization=latam02-lc-ml -Dsonar.projectKey=lc-ml -Dsonar.sources=. -Dsonar.host.url=https://sonarcloud.io'
            }
          }
    }
    stage("Quality Gate") {
       steps {
          timeout(time: 1, unit: 'HOURS') {
            waitForQualityGate abortPipeline: true
          }
        }
    }
  }
} 