FROM python:3.12-slim

WORKDIR /app

# cowsay paketini sisteme kurup gereksiz önbellekleri siliyoruz
RUN apt-get update && apt-get install -y --no-install-recommends cowsay \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Testler başarılı biterse arkasından ineği konuşturuyoruz
CMD ["sh", "-c", "pytest tester/ -v --cov=kalkylator --cov-report=term-missing && /usr/games/cowsay 'ALL TESTS PASSED!'"]
