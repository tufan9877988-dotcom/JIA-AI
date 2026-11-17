import os
import requests
from core.voice import speak
​PI_URL = os.getenv("JIA_API_URL")
PI_KEY = os.getenv("JIA_API_KEY")
​def ask_jia(question):
if not PI_URL or not API_KEY:
return "JIA API is not configured"
try:
response = requests.post(
PI_URL,
headers={
"Authorization": f"Bearer {PI_KEY}",
"Content-Type": "application/json"
},
json={
"model": os.getenv("JIA_MODEL", "YOUR_MODEL"),
"messages": [
{"role": "user", "content": question}
]
},
timeout=60
)
response.raise_for_status()
response_json = response.json()
answer = response_json['choices'][0]['message']['content']
speak(answer)
return answer
except Exception as e:
print("Voice Error:", e)
return f"JIA Error: {e}"
