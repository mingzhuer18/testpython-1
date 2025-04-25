pipeline {
    agent any
//     triggers {
//         githubPush() // 声明由 GitHub Push 事件触发
//     }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // 自动拉取触发构建的提交
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building..." && sleep 5' // 替换为实际构建命令
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..." && sleep 3'
            }
        }
    }
    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}