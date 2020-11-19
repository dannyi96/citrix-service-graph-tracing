docker build -t sales-portal .
docker tag sales-portal $1
docker push $1