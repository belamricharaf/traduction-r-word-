from deep_translator import GoogleTranslator

def translate_text(text: str, source: str, target: str) -> str:
    try:
        return GoogleTranslator(source=source, target=target).translate(text)
    except Exception as e:
        return f"Erreur: {e}"
