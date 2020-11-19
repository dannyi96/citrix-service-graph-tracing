export CPX_CLUSTER_IP=$(kubectl get service cpx-ingress -o jsonpath='{.spec.clusterIP}')

#!/bin/sh
while true
do
curl http://$CPX_CLUSTER_IP/tv-shows -H "Host: netflix-frontend-service"
sleep 3 
curl http://$CPX_CLUSTER_IP/tv-shows -H "Host: netflix-frontend-service"
sleep 3
curl http://$CPX_CLUSTER_IP/movies -H "Host: netflix-frontend-service"
sleep 3
curl http://$CPX_CLUSTER_IP/recommendation-engine?type=trending -H "Host: netflix-frontend-service"
sleep 3
curl http://$CPX_CLUSTER_IP/recommendation-engine?type=similar-shows -H "Host: netflix-frontend-service"
sleep 3
curl http://$CPX_CLUSTER_IP/recommendation-engine?type=mutual-friends-interests -H "Host: netflix-frontend-service"
sleep 3
curl http://$CPX_CLUSTER_IP/recommendation-engine?type=best-shows -H "Host: netflix-frontend-service"
sleep 3
done