# Imagen base
FROM python:3.12-slim

# Evita prompts durante instalación
ENV DEBIAN_FRONTEND=noninteractive

# Crear directorio de trabajo
WORKDIR /app

# Instalacioon dependencias sistema requeridas
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia,instala dependencias Python
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --progress-bar off


# Copia código fuente
COPY app ./app

# Expone puerto FastAPI
EXPOSE 8000

# Comando inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
