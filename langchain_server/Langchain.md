# 相关API

~~~txt
deepseek:
BASE_URL = "https://api.deepseek.com/v1"
OPENAI_API_KEY = "sk-8615b7b0f4f241239ef4c80a716b7588"

base_url = "https://api.deepseek.com/v1"
api_key = "sk-8615b7b0f4f241239ef4c80a716b7588"
~~~

# langchian提示词工程

~~~python
1.# 字符串提示词模板_____________________________________________________________
prompt_template = PromptTemplate.from_template("帮我写一篇20字的诗歌，关于{content}")

messages1 = prompt_template.format(content="春天")
2.# 聊天提示词模板（三个角色：system、hunman、assistant）_____________________________________________________________________
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个智能体专家，你的名字叫{name}。"),
        ("human", "专家你好，我有问题"),
        ("assistant","愚蠢的大学生，请抛出你的疑问"),
        ("human","{user_input}")

    ]
)
messages2 = chat_template.format_messages(name="大卫", user_input="langchain对智能体有什么用？")

3.# 该模板还可以传对象_____________________________________________________________________
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=("你是一个擅长对内容润色的助手")
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)
messages2 = chat_template.format_messages(text="langchain发展迅速")

~~~



