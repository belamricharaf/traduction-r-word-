from fastapi import FastAPI, Header, HTTPException
from models import TranslationRequest
from translation import translate_text

app = FastAPI()
API_KEY = "123456789-SECRET"

@app.post("/translate")
def translate(req: TranslationRequest, authorization: str = Header(...)):
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(403, "Clé API invalide")
    translated = translate_text(req.text, req.source_language, req.target_language)
    return {"translated_text": translated}
