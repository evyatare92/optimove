pipeline
{
    agent any
    stages
    {
        stage("build") {
            steps{
                sh script: "docker-compose -f src/docker-compose.yml build"
            }
        }
        stage("push to dockerhub"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-hub',usernameVariable: 'DOCKERHUB_USER',passwordVariable: 'DOCKERHUB_PASSWORD')]){
					sh script: "docker login -u  ${DOCKERHUB_USER} -p ${DOCKERHUB_PASSWORD}"		
				}
				sh script: "docker-compose -f src/docker-compose.yml push"
            }
        }
        stage("deploy to kubernetes"){
            steps{
                sh script: "helm upgrade ip-reverse helm/ip-reverse --kubeconfig C:/Users/evyat/.kube/config"
            }
        }
    }
}