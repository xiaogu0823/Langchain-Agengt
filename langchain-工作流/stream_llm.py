from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()  
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")
print(f"环境变量验证: API_KEY = {'已设置' if api_key else '未设置'}")

client = ChatOpenAI(
    model="deepseek-chat",  
    openai_api_key=api_key,  
    openai_api_base=base_url,
    streaming=True
)

chunks = []
for chunk in client.stream("今天天气怎么样？"):
    chunks.append(chunk)
    print(chunk.content, end="|",flush=True)

response = client.chat.completions.create(
  model="deepseek-chat",  
  messages=[{"role": "user", "content": "今天天气怎么样？"}]
)
print(response.choices[0].message.content)
