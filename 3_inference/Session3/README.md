# Welcome to NVIDIA AI Developers day!

## Docker build
$docker build -f Dockerfile --tag=deepstream:4.0.1-19.09-devel .

## Docker run

$docker run --runtime=nvidia --shm-size=256m --ipc=host --net=host -it -p 8888:8888  -v <tlt mount path>:/tlt-experiments -w /root deepstream:4.0.1-19.09-devel


## Run jupyter notebook
$/workspace/examples/ssd$ jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' --allow-root

## Go to URL
http://{your server ip}:8888/notebooks/deepstream_ssd.ipynb
