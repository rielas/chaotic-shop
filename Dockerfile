FROM python:3.13-slim

RUN apt-get update && apt-get install -y curl gpg

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY src/ src/
COPY tests/ tests/
COPY README.md ./
COPY public/ public/

RUN poetry install

ENTRYPOINT ["poetry", "run", "chaotic_shop"]
