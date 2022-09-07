FROM python:3.8.0
CMD mkdir app
WORKDIR app

RUN apt-get update && pip install pip --upgrade
COPY . .
RUN pip install -r requirements.txt   