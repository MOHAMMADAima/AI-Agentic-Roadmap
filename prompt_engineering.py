from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content

# Technique 1 : Zero-shot (pas d'exemple)
print("=== ZERO-SHOT ===")
print(ask(
    "Tu es un assistant utile.",
    "Classe ce texte comme positif ou négatif : 'Ce produit est incroyable'"
))

# Technique 2 : Few-shot (avec exemples) => prompt plus élaboré avec des exemples pour guider le modèle
print("\n=== FEW-SHOT ===")
print(ask(
    """Tu es un classificateur de sentiment.
    Exemples :
    'J'adore ce produit' -> positif
    'Ce service est nul' -> négatif
    'Ça fait le travail' -> neutre""",
    "Classe ce texte : 'Ce produit est incroyable'"
))

# Technique 3 : Chain of thought (raisonnement étape par étape)
print("\n=== CHAIN OF THOUGHT ===")
print(ask(
    "Tu es un assistant. Raisonne étape par étape avant de répondre.",
    "Si j'ai 3 réunions de 45 min et 2 pauses de 10 min dans ma journée, combien de temps total ça prend ?"
))