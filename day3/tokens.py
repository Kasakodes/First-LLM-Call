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
prompt1="Do you know Carry Minati?"
prompt2="Do you know kasak Jain?"
prompt3="What is the capital of India?"
prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    message={
        "role": role,
        "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages, max_tokens=50)
    print(response.choices[0].message.content)
    usage=response.usage
    print(f"Prompt Tokens: {usage.prompt_tokens}, Completion Tokens: {usage.completion_tokens}, Total Tokens: {usage.total_tokens}, Finish reason: {response.choices[0].finish_reason}")


