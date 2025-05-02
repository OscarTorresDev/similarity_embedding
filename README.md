Similarity_embedding

API REST que genera embeddings y calcula la similitud coseno entre dos frases usando FastAPI y el modelo sentence-transformers/all-MiniLM-L6-v2.

Requisitos
Docker (recomendado)
(Opcional) Python 3.9+ y pip si deseas ejecutar localmente

```markdown
# Similarity API - AI Joes LLC

Este proyecto es una API REST desarrollada con FastAPI que permite obtener el embedding de una frase y calcular la similitud entre dos textos usando el modelo `all-MiniLM-L6-v2` de Sentence Transformers. 

Fue desarrollado como parte de una prueba técnica en abril de 2025.

## ¿Qué hace esta API?

1. Genera un *embedding* numérico a partir de una frase.
2. Calcula la similitud entre dos frases usando la **similitud de coseno**.
---

## Cómo ejecutar la API con Docker

### 1. Clonar el repositorio

```bash
git clone https://github.com/OscarTorresDev/similarity_embedding
cd similarity_embedding
````

### 2. Construir la imagen

```bash
docker build -t similarity-api .
```

### 3. Ejecutar el contenedor

```bash
docker run -p 8000:8000 similarity-api
```

La API quedará disponible en: [http://localhost:8000](http://localhost:8000)

---

## Endpoints disponibles

### 1. Obtener embedding

**POST** `/embed`

**Ejemplo con `curl`:**

```bash
curl -X POST http://localhost:8000/embed \
     -H "Content-Type: application/json" \
     -d '{"text": "Hola mundo"}'
```

**Respuesta esperada:**

```json
{
  "embedding": [-0.041,0.139,...]
}
```

---

### 2. Calcular similitud entre dos textos

**POST** `/similarity`

**Ejemplo con `curl`:**

```bash
curl -X POST http://localhost:8000/similarity \
     -H "Content-Type: application/json" \
     -d '{"text1": "Hola, ¿cómo estás?", "text2": "Buenos días, mucho gusto"}'
```

**Respuesta esperada:**

```json
{
  "similarity_score": 0.54
}
```

---

## Alternativa: usar `client.py`

También puedes usar el archivo `client.py` incluido para probar los endpoints:

```bash
python client.py
```

Este script realiza:

* Una solicitud de embedding para la frase "Hola mundo"
* Un cálculo de similitud entre "Hola, ¿cómo estás?" y "Buenos días, mucho gusto"

---

## Requisitos

Si deseas correrlo sin Docker, asegúrate de tener Python 3.10 o superior y ejecuta:

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload
```

---

## Notas adicionales

* El modelo se carga una sola vez al iniciar la API para optimizar el rendimiento.
* Las respuestas incluyen valores de precisión flotante para facilitar su análisis.

---

Desarrollado por Oscar para la prueba técnica M J M - Abril 2025.


