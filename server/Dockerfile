FROM python:3.9

ADD . /app
WORKDIR /app

# RUN apt update
# RUN apt -y upgrade
# RUN apt -y install python3 python3-pip
RUN pip3 install -r requirements.txt

CMD python3 server.py 0.0.0.0:9000