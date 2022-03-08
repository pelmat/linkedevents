FROM python:3.7-buster AS appbase
FROM appbase AS linked_setup

ENV APP_NAME linkedevents
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV STATIC_ROOT /var/www/static/
ENV MEDIA_ROOT /var/www/media/

RUN adduser --disabled-login --no-create-home --gecos '' linkedevents
WORKDIR /srv/app
COPY . .

RUN apt-get update && apt-get install -y postgresql-client less netcat-openbsd gettext locales gdal-bin python-gdal python3-gdal

RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r deploy/requirements.txt --no-cache-dir

RUN python manage.py compilemessages
RUN python manage.py collectstatic --no-input

ENTRYPOINT ["./docker-entrypoint.sh"]

FROM linked_setup AS development
ENV PRODUCTION=0
ENV DEBUG=True

FROM linked_setup AS production
ENV PRODUCTION=1
ENV DEBUG=False
USER linkedevents
EXPOSE 8000/tcp