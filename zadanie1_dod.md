## 4. Wykorzystanie kodu z publicznego repozytorium
# Dockerfile:
# syntax=docker/dockerfile:1.2
FROM python:3.9-slim

# Instalacja Git i innych zależności
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Instalacja zależności Python
RUN pip install --no-cache-dir httpserver

# Ustawienie katalogu roboczego
WORKDIR /usr/src/app

# Klonowanie repozytorium z GitHub
RUN git clone https://github.com/slanedrv/DockerZad1 .

# Informacje o autorze
LABEL maintainer="Imię Nazwisko"

# Otwarcie portu
EXPOSE 8000

# Polecenie do uruchomienia serwera
CMD ["python", "server.py"]

# Polecenia do budowy i wysyłki obrazów:
docker buildx create --use --name mybuilder

docker buildx use mybuilder

docker buildx inspect --bootstrap

docker buildx build --platform linux/amd64,linux/arm64 --cache-to=type=local,dest=./cache --cache-from=type=local,src=./cache -t slanedrv/myserver:latest --push .
