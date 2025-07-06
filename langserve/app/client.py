
from langchain.schema.runnable import RunnableMap
from langserve import RemoteRunnable
from langchain.prompts import ChatPromptTemplate


dpsk = RemoteRunnable("http://localhost:8000/deepseek/")
prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个喜欢写故事的助手"), ("user","故事主题是{topic}")]
)

# 自定义chain
chain = prompt | RunnableMap({
    "deepseek":dpsk
})

# print("同步调用/dspk/invoke结果")
# response = chain.invoke([{"topic":"猫"}])
# print(response)

# 链式流式
# dpsk_str_parser = RemoteRunnable("http://localhost:8000/deepseek/stream")
# chain_str_parser = prompt | RunnableMap({
#     "deepseek": dpsk_str_parser,

# })
# print("测试StrOutputParser")
# response = chain_str_parser.stream({"topic": "猫"})
# print(response)

for chunk in chain.stream({"topic": "猫"}):
    print(chunk, end="", flush=True)
    print(chunk["deepseek"].content, end="", flush=True)
