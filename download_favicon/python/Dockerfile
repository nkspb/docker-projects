FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN mkdir /downloads && pip3 install -r requirements.txt 
CMD python3 ./app.py $URL
