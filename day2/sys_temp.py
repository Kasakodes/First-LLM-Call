import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-20b"
role="user"
prompt="I love you, baby"
message_system={
    'role': 'system',
    'content': 'You are a helpful assistant that translates English to French.'
}
message={
    "role": role,
    "content": prompt
}
messages=[message_system, message]
# Temperature is bydefault set to 0.
response=client.chat.completions.create(model=model, messages=messages, temperature=1)
print(response.choices[0].message.content)


