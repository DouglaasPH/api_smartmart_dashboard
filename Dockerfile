
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências de sistema (psycopg2 precisa disso)
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install --no-cache-dir poetry==2.0.1
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --no-ansi

# Copia o restante do projeto
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
