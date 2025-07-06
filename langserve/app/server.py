from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from langchain_core.runnables import RunnableLambda
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")
print(f"环境变量验证: API_KEY = {'已设置' if api_key else '未设置'}")

app = FastAPI(
    title="LangServe 练手应用项目",
    description="这是一个使用 LangServe 和 LangChain 创建的示例应用，演示如何构建和部署可交互的 LLM 应用。",
    version="1.0.0",
    # openapi_url="/openapi.json",
    # docs_url="/docs",
    # redoc_url=None,  # 禁用 ReDoc 文档
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

# # 方法1：
# # 创建示例 Runnable 链 （可自定义）
# def hello_world(input: dict) -> dict:
#     """简单的示例函数，返回问候语"""
#     name = input.get("name", "World")
#     return {"message": f"Hello, {name}!"}

# # 创建可运行的链
# hello_runnable = RunnableLambda(hello_world)

# 方法2
# 或者使用 LangChain 组件创建更复杂的链
# prompt = ChatPromptTemplate.from_template("给我讲一个笑话，话题关于 {topic}")
# model = ChatOpenAI(api_key=api_key, openai_api_base=base_url, model="deepseek-chat", streaming=True)  
# joke_chain = prompt | model

""" 添加路由 到 FastAPI 应用
1. add_routes 函数会自动处理 /hello 或 /joke 的路由，并提供一个交互式的 Playground 界面
2.可以通过访问 http://localhost:8000/docs 来查看和测试这些端点 注意：确保已安装 langserve 和 langchain_openai 库，并且已设置环境变量 OPENAI_API_KEY
3.使用 API，需要确保设置了 API_KEY 和 BASE_URL 环境变量
"""

add_routes(
    app,
    path="/deepseek",
    runnable=ChatOpenAI(
        model="deepseek-chat",  # 使用 DeepSeek 的聊天模型
        openai_api_key=api_key,  # 从环境变量获取 API 密钥
        openai_api_base=base_url,  # 从环境变量获取 API 基础 URL
        streaming=True  # 启用流式响应
    ),
    playground_type="chat",  # 启用聊天界面
)
# add_routes(
#     app,
#     hello_runnable,  # 使用简单的 hello_world 函数
#     path="/hello",  # 访问 http://localhost:8000/hello
#     playground_type="chat"  # 启用聊天界面
# )

# add_routes(
#     app,
#     joke_chain,  # 使用 LangChain 创建的笑话链
#     path="/joke",   # 访问 http://localhost:8000/joke
#     playground_type="chat"  
# )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)