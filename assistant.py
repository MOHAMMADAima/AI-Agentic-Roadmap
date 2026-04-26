from groq import Groq
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --- OUTILS ---
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Retourne la date et l'heure actuelle",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Effectue un calcul mathématique simple",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "L'expression mathématique à calculer ex: 2+2"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

def get_current_time():
    return datetime.now().strftime("%d/%m/%Y à %H:%M")

def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Expression invalide"

def handle_tool_call(tool_name, args):
    if tool_name == "get_current_time":
        return get_current_time()
    elif tool_name == "calculate":
        return calculate(args.get("expression", ""))

# --- ASSISTANT ---
messages = [
    {"role": "system", "content": """Tu es un assistant personnel utile et concis. 
    Tu as accès à des outils pour donner l'heure et faire des calculs."""}
]

print("=== Assistant Personnel ===")
print("Tape 'quit' pour quitter\n")

while True:
    user_input = input("Toi : ")
    if user_input.lower() == "quit":
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=0.7,
            max_tokens=300
        )

        message = response.choices[0].message

        # Si le LLM appelle un outil
        if message.tool_calls:
            tool_call = message.tool_calls[0]
            args = json.loads(tool_call.function.arguments)
            result = handle_tool_call(tool_call.function.name, args)

            print(f"[Outil utilisé : {tool_call.function.name}]")

            # On remet le résultat dans la conversation
            messages.append({"role": "assistant", "content": None, "tool_calls": message.tool_calls})
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

            # Réponse finale avec le résultat de l'outil
            final_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.7,
                max_tokens=300
            )
            assistant_reply = final_response.choices[0].message.content
        else:
            assistant_reply = message.content

        messages.append({"role": "assistant", "content": assistant_reply})
        print(f"\nAssistant : {assistant_reply}\n")

    except Exception as e:
        print(f"Erreur : {e}")