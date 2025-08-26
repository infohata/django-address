FROM python:3.11-slim
LABEL maintainer="infohata@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    LANG=C.UTF-8

RUN    apt-get -qq update \
    && apt-get -y install \
        bash \
        locales \
        git \
        build-essential \
        libssl-dev \
    && ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && locale-gen C.UTF-8 || true

RUN mkdir -p /code
WORKDIR /code
COPY ./example_site /code/
COPY ./address /code/address
RUN pip install -r /code/requirements.txt
EXPOSE 8000
CMD ./wait_for_postgres.py && ./manage.py migrate && ./manage.py runserver 0.0.0.0:8000
