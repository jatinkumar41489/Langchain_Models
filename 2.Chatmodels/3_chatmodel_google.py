
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_output_tokens=100
)

result = model.invoke("What is the capital of India?")

#result.content → poori list
#result.content[0] → pehla content block
#result.content[0]["text"] → sirf actual answer
print(result.content[0]["text"])
