FROM python:3.8-slim-buster

WORKDIR /prj

RUN pip3 install flask

COPY app/ /prj/
EXPOSE 3000
CMD [ "python3", "/prj/main.py"]