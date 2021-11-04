pipeline {
  agent any
  environment{
    SONAR_TOKEN = credentials('sonar_token')
    DOCKER_USER = 'lcarrieta'
    DOCKER_PASSWORD = credentials('docker_pass')
    IMAGE_NAME ='ml-lc'
    TAG_VERSION = '1.4'
  }
  stages {
    // stage('UnitTest') {
    //   agent {
    //     docker { 
    //       image 'crgv/tensorflow-c:2.6.2'
    //       }
    //   }
    //   steps { 
    //       sh 'pip install --upgrade pip'
    //       sh 'pip install -r requirements-dev.txt --no-cache-dir'
    //       sh 'python -m pytest --html=report.html -s'
    //   }
    //   post {
    //     always {
    //       archiveArtifacts artifacts: '**/*.html', followSymlinks: false
    //     }
    //   }
    // }
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
    // stage('Package') {
    //   steps {
    //     sh 'docker build -t ${IMAGE_NAME}:${TAG_VERSION} .'
    //   }
    // }
    // stage('Publish') {
    //   steps {
    //     sh 'docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}'
    //     sh 'docker tag ${IMAGE_NAME}:${TAG_VERSION} ${DOCKER_USER}/${IMAGE_NAME}:${TAG_VERSION}'
    //     sh 'docker push ${DOCKER_USER}/${IMAGE_NAME}:${TAG_VERSION}'
    //   }
    // }
    // stage('Deploy') {
    //   steps {
    //     sh 'docker-compose up -d'
    //   }
    // }
  }
} 