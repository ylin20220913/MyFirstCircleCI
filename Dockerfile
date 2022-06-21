FROM python:3.7

WORKDIR /home/

COPY ./ ./

CMD [ "sh", "./run-robot.sh"]

# Run dockerfile
# sudo docker build -t docker-test .
# sudo docker run --rm --privileged docker-test