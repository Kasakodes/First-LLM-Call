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

#structure the prompt and message for the chat completion
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
    
schema=Ticket.model_json_schema()
    
response_format={
    "type": "json_object"
}
system_Prompt=f"""
Extra the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""
message_system={
    "role": "system",
    "content": system_Prompt
}
text="Hello, my name is John Doe. My email is john.doe@example.com. I have an issue with my account."
prompt=f"""
this is a customer ticket. Please extract the personal information from this.
{text}
"""
#define role and content in message
message={
    "role": role,
    "content": prompt
}
messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer=response.choices[0].message.content
print(answer)

#isko pdhte kaise h?
#json string to python dict me convert karne ke liye aap json module ka use kar sakte hain. Aapko bas json.loads() function ka use karna hoga. Yahan ek example diya gaya hai:
import json
raw_json_string = answer  # yahan aapka json string hoga
data_file=json.loads(raw_json_string)
ticket=Ticket(**data_file)


print(ticket.name)
print(ticket.email)
print(ticket.issue)


