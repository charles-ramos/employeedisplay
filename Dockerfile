FROM python:3
WORKDIR /app
COPY requirements.txt /app/
EXPOSE 8000
RUN pip install -r requirements.txt