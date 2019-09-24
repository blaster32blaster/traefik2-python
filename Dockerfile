FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["flask", "run"]


# FROM python:2.7.16
# WORKDIR /app
#ENV BUILD_DEPS="build-essential vim" \
#    APP_DEPS="curl libpq-dev"
# RUN apt-get update \
#  && apt-get install -y ${BUILD_DEPS} ${APP_DEPS} --no-install-recommends \
#  && apt-get update && apt-get install -qqy git unzip libfreetype6-dev \
#        libjpeg62-turbo-dev \
#        libpng-dev \
#        default-mysql-client \
#        libaio1 wget