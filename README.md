# daniel
usage:
build an image with:
docker build . -t ${image_name}
run the container with:
docker run -d --network host 
test using:
curl localhost:80/daniel