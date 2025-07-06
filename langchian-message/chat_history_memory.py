from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory

# 定义聊天模板
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.you're good at {ability}.Respond in Chinese."),
     # 历史消息占位符
     MessagesPlaceholder(variable_name="history"),("human","{input}"),
     ]
)

model = ChatOpenAI()
runnable = prompt | model

# 模拟存储会话历史的字典
store = {}

# 定义获取历史会话记录，入参是session_id，返回一个对话历史记录
def get_session_history(session_id:str) -> BaseChatMessageHistory:
    """获取会话历史"""
    # 如果当前 session_id 不在 store（历史记录存储字典）中
    if session_id not in store:
        # 就为这个 session_id 初始化一个空的聊天历史记录
        store[session_id] = ChatMessageHistory()
    
    # 返回该 session_id 对应的聊天历史记录（无论是已有的还是刚创建的）
    return store[session_id]

# 创建一个带会话历史记录的Runnable
with_message_history = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
    )

response = with_message_history.invoke(
    {"ability":"math","input":"余弦是什么意思？"},
    config={"confiigurable":{"session_id":"123"}}
        )

print(response)

# 再次调用同一个会话ID
# 这次会话历史会被自动添加到消息中
response = with_message_history.invoke(
    {"ability":"math","input":"什么？"},  
    config={"confiigurable":{"session_id":"123"}}
        )
print(response)

# 再次调用不同的会话ID，隔绝会话历史
response = with_message_history.invoke(
    {"ability":"math","input":"什么？"},
    config={"confiigurable":{"session_id":"123456"}}
        )
print(response)