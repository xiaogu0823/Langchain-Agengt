#MessagesPlaceHolder负责在特定位置添加消息列表
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个ai智能体"),
        # 此处传入消息
        MessagesPlaceholder("msgs")
    ]
)
result = prompt_template.invoke({"msgs":[HumanMessage(content="Hi !")]})
print(result)