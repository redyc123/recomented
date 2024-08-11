FROM python:3.11-slim

COPY ./src/ /srv/
COPY ./data/ /data/

WORKDIR /srv/

RUN apt update && \
    apt -y full-upgrade && \
    pip install --upgrade pip poetry==1.5.1 && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction --no-ansi --no-root

CMD  ["python", "srv.py"]