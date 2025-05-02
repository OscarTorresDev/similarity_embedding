
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

app = FastAPI()

# Carga el modelo una sola vez
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

class TextRequest(BaseModel):
    text: str

class SimilarityRequest(BaseModel):
    text1: str
    text2: str

@app.post("/embed")
def embed_text(req: TextRequest):
    emb = model.encode(req.text)
    return {"embedding": emb.tolist()}



@app.post("/similarity")
def calc_similarity(req: SimilarityRequest):
    emb1 = model.encode(req.text1)
    emb2 = model.encode(req.text2)
    score = float(util.cos_sim(emb1, emb2).item())
    return {"similarity_score": score}