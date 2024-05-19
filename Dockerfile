# Podstawowy obraz
FROM python:3.9-slim

# Instalacja zależności
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Ustawienie katalogu roboczego
WORKDIR /usr/src/app

# Kopiowanie kodu źródłowego
RUN git clone https://github.com/slanedrv/DockerZad1 .

# Informacja o autorze
LABEL maintainer="Dzmitry Revutski"

# Otwarcie portu
EXPOSE 8000

# Komenda do uruchomienia serwera
CMD ["python", "server.py"]

