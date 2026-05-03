FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install uv
RUN uv sync

RUN chmod +x /app/docker/django/entrypoint.sh

EXPOSE 8000
