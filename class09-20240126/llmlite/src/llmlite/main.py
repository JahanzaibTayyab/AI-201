from litellm import completion
import os

os.environ["GEMINI_API_KEY"]
os.environ['GROQ_API_KEY']

model1="gemini/gemini-1.5-flash"
messages1=[
    {
        "role": "user",
        "content": "Write a paragraph about AI"
    }
  ]

def gemini():    
    response1 = completion(model1, messages=messages1)
    print(response1)


model2="groq/llama3-8b-8192"
messages2=[
    {
        "role": "user",
        "content": "Write a paragraph about AI"
    }
  ]

def groq():    
    response2 = completion(model2, messages=messages2)
    print(response2['choices'][0]['message']['content'])


