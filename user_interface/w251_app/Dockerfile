# Base Arguements to leverage across build stages
ARG APP_DIR=/app


#############
# Deployment image
#############
FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3 as run 
ARG APP_DIR

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
WORKDIR ${APP_DIR}/
COPY  . ./


RUN apt update && apt install -y  libssl-dev
RUN pip3 install -U pip

RUN apt update && apt install -y libffi-dev python3-pip curl unzip python3-tk libopencv-dev python3-opencv 
RUN pip3 install -U gsutil pyyaml tqdm cython #torchvision   
RUN apt install -y python3-scipy python3-matplotlib python3-numpy
RUN apt-get update && apt-get install libgl1
RUN pip3 install git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI
RUN pip list

RUN pip3 install -r requirements.txt
RUN curl https://cloudobjectstorage.s3.us-west-1.amazonaws.com/best.pt --output ../best.pt
HEALTHCHECK --start-period=30s CMD python -c "import requests; requests.get('http://localhost:8000/health', timeout=2)"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
