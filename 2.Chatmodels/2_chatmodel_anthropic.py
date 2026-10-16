from langchain import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

ChatAnthropic(
    model="claude-3.0",
    temperature=0.7,
    max_completion_tokens=100
)

result=model.invoke("What is a Large Language Model?")

print(result.content)

