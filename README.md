# 🚀 Similarity API

API REST que genera *embeddings* y calcula la similitud coseno entre dos frases usando [FastAPI](https://fastapi.tiangolo.com/) y el modelo `sentence-transformers/all-MiniLM-L6-v2`.

---

## 📦 Requisitos

- Docker (recomendado)
- (Opcional) Python 3.9+ y pip si deseas ejecutar localmente

---

## 🐳 Ejecutar con Docker

```bash
# Construir la imagen desde la carpeta raíz del proyecto
docker build -t similarity-api .

# Ejecutar el contenedor exponiendo el puerto 8000
docker run -p 8000:8000 similarity-api


---

## 🐍 Ejemplo de cliente en Python

También puedes probar la API usando un pequeño script Python:

### Paso 1: Instala `requests` si no lo tienes

```bash
pip install requests
