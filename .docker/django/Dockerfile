FROM python:3.8-slim

RUN adduser --disabled-password --disabled-login --gecos "" django
USER django

WORKDIR /home/django/app/

ENV PATH="/home/django/.local/bin:$PATH"

COPY --chown=django:django requirements.txt /home/django/app/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY --chown=django:django . /home/django/app/
