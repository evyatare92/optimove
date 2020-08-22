pipeline
{
    agent any
    stages
    {
        stage("build") {
            steps{
                bat script: "docker-compose build -f src/socker-compose.yml"
            }
        }
        stage("push to dockerhub"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-hub',usernameVariable: 'DOCKERHUB_USER',passwordVariable: 'DOCKERHUB_PASSWORD')]){
					bat script: "docker login -u  ${DOCKERHUB_USER} -p ${DOCKERHUB_PASSWORD}"		
				}
				bat script: "docker-compose push -f src/socker-compose.yml"
            }
        }
        stage("deploy to kubernetes"){
            steps{
                bat script: "helm upgrade ip-reverse ./helm/ip-reverse --kubeconfig C:/Users/evyat/.kube/config"
            }
        }
    }
}