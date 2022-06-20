FROM python:3.7

WORKDIR /home/robot/test

COPY ./ ./

RUN pip install RPi.GPIO

CMD [ "sh", "./run-robot.sh"]

# Run dockerfile
# sudo docker build -t docker-test .
# sudo docker run --rm --privileged docker-test