FROM python:latest

LABEL Maintainer="rypy"

WORKDIR /usr/app/src

COPY currentProcess.py ./

CMD [ "python3", "./currentProcess.py"]