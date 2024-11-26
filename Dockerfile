FROM python:3.9

# Kopiuje pliki aplikacji
COPY . /app

# Katalog roboczy
WORKDIR /app

# Zainstaluj zależności
RUN pip install fastapi pydantic scikit-learn uvicorn

# Otwórz port
EXPOSE 8000

# Uruchom serwer
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
