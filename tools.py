from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Définition de l'outil
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Obtenir la météo d'une ville",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Le nom de la ville"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# Fausse fonction météo (on simule une vraie API)
def get_weather(city):
    meteo_simulee = {
        "Paris": "18°C, ensoleillé",
        "Lyon": "15°C, nuageux",
        "Marseille": "22°C, ensoleillé"
    }
    return meteo_simulee.get(city, "Ville non trouvée")

# Appel avec tool
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Quel temps fait-il à Paris ?"}
    ],
    tools=tools,
    tool_choice="auto"
)

# Traitement de la réponse
message = response.choices[0].message

if message.tool_calls:
    tool_call = message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = get_weather(args["city"])
    print(f"Outil appelé : {tool_call.function.name}")
    print(f"Argument : {args}")
    print(f"Résultat : {result}")
else:
    print(message.content)