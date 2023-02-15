FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
EXPOSE 8080
RUN pip install -r requirements.txt
