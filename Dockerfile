FROM python:3.12-slim

# Evita prompts durante instalación
ENV DEBIAN_FRONTEND=noninteractive

# Crear directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependencias de Python
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --progress-bar off


# Copia el código fuente
COPY app ./app

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
