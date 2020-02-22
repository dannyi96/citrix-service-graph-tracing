# Build
docker build -t in-docker-reg.eng.citrite.net/cpx-dev/blog/accounts:v0.1 . -f Dockerfile_frontend

# Run
docker run -d -p 80:7500 --name blog-exmpl in-docker-reg.eng.citrite.net/cpx-dev/blog/accounts:v0.1
