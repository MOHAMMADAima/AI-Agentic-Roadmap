from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": "Tu es un assistant utile et concis."}
]

print("Chatbot démarré. Tape 'quit' pour quitter.\n")

while True:
    user_input = input("Toi : ")
    
    if user_input.lower() == "quit":
        break
    
    messages.append({"role": "user", "content": user_input})
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )
        
        assistant_message = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_message})
        
        print(f"\nAssistant : {assistant_message}\n")
        
    except Exception as e:
        print(f"Erreur : {e}")