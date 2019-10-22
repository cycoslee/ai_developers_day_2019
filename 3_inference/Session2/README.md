# Welcome to NVIDIA AI Developers day!

## Docker build
docker build -f Dockerfile --tag=tlt:v1.0_py2 .

## Docker run
docker run --runtime=nvidia -it --shm-size=256m --ipc=host -p 8887:8888 -v <local mount path>:/workspace/tlt-experiments -w /workspace/examples/ssd tlt:v1.0_py2

## Run jupyter notebook
$/workspace/examples/ssd$ jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' --allow-root

## Go to URL
http://{your server ip}:8887/notebooks/tlt_ssd.ipynb

