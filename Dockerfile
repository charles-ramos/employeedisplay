FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /requirements.txt

RUN set -ex \
 && pip install --upgrade pip \
 && pip install --no-cache-dir -r /requirements.txt \
 && apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /app


EXPOSE 8000

CMD [ "python", "manage.py"]