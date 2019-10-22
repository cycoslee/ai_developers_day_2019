# Build the dockerfile for the engironment 
if [ ! -z $(docker images -q tensorrt_ssd:latest) ]; then
	echo "Dockerfile has already been built"
else
	echo "Building docker image"
	docker build -f dockerfiles/Dockerfile --tag=tensorrt_ssd .
fi

# Start the docker container
echo "Starting docker container"
docker run --runtime=nvidia -it -p 8886:8886 -p 6006:6006 -v `pwd`:/workspace/tensorrt_ssd tensorrt_ssd
