from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from langchain.prompts import HumanMessagePromptTemplate


# # 创建消息数组，此处定义了name和user_input参数
# # 字符串提示词模板_____________________________________________________________
# prompt_template = PromptTemplate.from_template("帮我写一篇20字的诗歌，关于{content}")

# messages1 = prompt_template.format(content="春天")
# print(messages1)


# # 聊天提示词模板（三个角色：system、hunman、assistant）_______________________
# chat_template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "你是一个智能体专家，你的名字叫{name}。"),
#         ("human", "专家你好，我有问题"),
#         ("assistant","愚蠢的大学生，请抛出你的疑问"),
#         ("human","{user_input}")

#     ]
# )
# # 该模板还可以传对象
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=("你是一个擅长对内容润色的助手")
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

# 通过模板参数

# messages2 = chat_template.format_messages(name="大卫", user_input="langchain对智能体有什么用？")
# print(messages2)
# """messages返回内容（报文）
# [SystemMessage(content='你是一个智能体专家，你的名字叫大卫。', additional_kwargs={}, response_metadata={}), HumanMessage(cont
# ent='专家你好，我有问题', additional_kwargs={}, response_metadata={}), AIMessage(content='愚蠢的大学生，请抛出你的疑问', addi
# tional_kwargs={}, response_metadata={}), HumanMessage(content='langchain对智能体有什么用？', additional_kwargs={}, response_m
# etadata={})]
# """
messages3 = chat_template.format_messages(text="langchain发展迅速")
print(messages3)
