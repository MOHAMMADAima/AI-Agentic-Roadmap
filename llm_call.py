from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.1-8b-instant", #ID of the model to use
    messages=[ # A list of messages comprising the conversation so far.
        {"role":"system", "content":"Tu es un assistant utile."},
        {"role":"user", "content" : "Explique- moi ce q'est un agent IA en 3 lignes."}
    ],
 

    temperature= 0.1, #What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both.
    max_tokens=200 #The maximum number of tokens that can be generated in the chat completion. The total length of input tokens and generated tokens is limited by the model's context length.
)

print(response.choices[0].message.content)
