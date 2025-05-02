import requests

BASE_URL = "http://localhost:8000"

def get_embedding(text):
    response = requests.post(f"{BASE_URL}/embed", json={"text": text})
    return response.json()

def get_similarity(text1, text2):
    response = requests.post(f"{BASE_URL}/similarity", json={"text1": text1, "text2": text2})
    return response.json()

if __name__ == "__main__":
    print("🔹 Obteniendo embedding para: 'Hola mundo'")
    embedding = get_embedding("Hola mundo")
    print("Embedding:", embedding)

    print("\n Similitud entre 'Hola, ¿cómo estás?' y 'Buenos días, mucho gusto'")
    similarity = get_similarity("Hola, ¿cómo estás?" , "Buenos días, mucho gusto")
    print("Similarity Score:", similarity)
