from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=OpenAIEmbeddings(model="text-embedding-3-large",dimension=32)

docs=[
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result=model.embed_documents(docs)

print(str(result))