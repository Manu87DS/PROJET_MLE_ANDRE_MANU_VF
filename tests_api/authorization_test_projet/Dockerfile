FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y
ADD authorization_test.py requirements.txt /app/
WORKDIR /app
RUN mkdir logs && pip3 install -r requirements.txt
CMD python3 authorization_test.py
