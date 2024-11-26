# Real Time Analytics

## Projekt zaliczeniowy
### Przedmoit  : ANALIZA DANYCH W CZASIE RZECZYWISTYM
### Sygnatura  : 22289
### Nr indeksu : 83580

## Anomaly Detection Service

### Opis
Serwis WWW do wykrywania anomalii wykorzystujacy modelu One-Class SVM, zbudowany przy użyciu FastAPI i wdrożony jako obraz Dockerowy.

### Instalacja
#### Wymagania
- Python
- Docker

#### Kroki instalacji
1. Sklonuj to repozytorium:
   ```bash
   git clone https://github.com/up7own8oy/RealTimeAnalytics

2. Uruchom serwis lokalnie:
   ```bash
   uvicorn app:app --reload

3. Otwórz przeglądarkę i przejdź do
    http://localhost:8000/docs.

#### Uruchamianie w Dockerze
1. Zbuduj obraz Dockerowy:
   ```bash
   docker build -t anomaly-detection-fastapi .

2. Uruchom kontener:
   ```bash
    docker run -p 8000:8000 anomaly-detection-fastapi
