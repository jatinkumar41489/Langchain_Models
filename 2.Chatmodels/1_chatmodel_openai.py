# FOR OPENAI
"""from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(
    model="gpt-4o", 
    temperature=0.7
    )

result=model.invoke("What is a Large Language Model?")
print(result) # this will give you the result in dictionary format.
print(result.content) #this will give you only the answer in string format.
"""

#TO USE NVIDIA AI ENDPOINTS
#You can get the API KEY or free from https://developer.nvidia.com/ai-endpoints


from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_completion_tokens=100
)

result = model.invoke("What is a Large Language Model?")

print(result)
print(result.content)
