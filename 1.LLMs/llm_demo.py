#FOR OPENAI --> We will use the OpenAI LLM to generate responses to user queries. Make sure to set your OPENAI_API_KEY in your environment variables before running this code.
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(
    model="here you need to define which gpt model you are using",
    temperature=0.7
)

response = llm.invoke("What is a Large Language Model?")
print(response.content)


