FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ARG ARG_CLOUD_LOCATION="A Cloud"
ENV CLOUD_LOCATION=$ARG_CLOUD_LOCATION
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]