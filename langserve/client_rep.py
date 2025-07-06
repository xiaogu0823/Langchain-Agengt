import requests
import json
from langchain.globals import set_debug, set_verbose
# 使用post时可以用postman测试接口
# 同步
# response = requests.post(
#     "http://localhost:8000/deepseek/invoke",
#     json={"input":{"topic": "猫"}}
# )

# print("同步调用/deepseek/invoke结果")
# print(response.json())

# 流式
response = requests.post(
    "http://localhost:8000/deepseek/invoke",
    json={"input":{"topic": "猫"}}
)

print("流式调用/deepseek/invoke结果")
for line in response.iter_lines():
    line = line.decode('utf-8')
    if line.startswith("data:") and line.endswith("[DOME]"):
        data = json.loads(line[len("data:"):])
        print(data)
