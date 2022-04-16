FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y
ADD main.py pretraitement.py model_logistic_regression.pkl model_gradient_boosting.pkl model_random_forest.pkl test.csv requirements.txt /app/
WORKDIR /app
RUN mkdir logs && pip3 install -r requirements.txt
CMD uvicorn main:api --host 0.0.0.0
