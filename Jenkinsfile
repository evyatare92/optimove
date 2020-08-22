pipeline
{
    agent any
    stages
    {
        stage("build") {
            steps{
                sh script: "docker-compose build -f src/socker-compose.yml"
            }
        }
        stage("push to dockerhub"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-hub',usernameVariable: 'DOCKERHUB_USER',passwordVariable: 'DOCKERHUB_PASSWORD')]){
					sh script: "docker login -u  ${DOCKERHUB_USER} -p ${DOCKERHUB_PASSWORD}"		
				}
				sh script: "docker-compose push -f src/socker-compose.yml"
            }
        }
        stage("deploy to kubernetes"){
            steps{
                sh script: "helm upgrade ip-reverse ./helm/ip-reverse --kubeconfig /home/jenkins/.kube/config"
            }
        }
    }
}