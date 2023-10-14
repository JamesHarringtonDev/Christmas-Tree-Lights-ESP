# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# copy all the files over, install requirements
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


# final configuration
CMD ["python3", "src/helloWorld.py"]