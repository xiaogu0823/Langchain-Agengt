# 给模型少量示例，避免模型出现幻觉
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
# 准备示例数据（必须包含input和content）
examples = [
    {
        "input":"导入 ConversationBufferMemory 时出现导入错误，如何解决？",
        "content":"该组件已从 langchain 迁移到 langchain_community"
    },
    {
        "input":"如何搭建一个链来抓取网页并生成摘要？",
        "content":
            """
            from langchain_community.document_loaders import WebBaseLoader
            from langchain_openai import ChatOpenAI
            from langchain_core.prompts import PromptTemplate
            from langchain_core.output_parsers import StrOutputParser

            # 网页加载器
            loader = WebBaseLoader("https://example.com")
            docs = loader.load()

            # 摘要链
            prompt = PromptTemplate.from_template("用50字总结内容：{text}")
            chain = prompt | ChatOpenAI() | StrOutputParser()

            # 执行
            summary = chain.invoke({"text": docs[0].page_contetextnt})
            print(f"摘要：{summary}")

            """
    },
    {
        "input":"调用 .predict() 方法时出现属性错误？",
        "content":"新版 LangChain 已弃用 .predict()，改用统一调用接口.invoke()"
    }
]
#input_variables用于在提示词模板后追加内容，用于定义suffix中包含的模板参数
# template定义参数占位
example_prompt = PromptTemplate(input_variables=["input", "content"], template="问题：{input}\\n回答: {content}")
# example[0] = {'question':'...','answer':'...'},此处格式化处理，加**是把内容从字典中解构出来'question':'...','answer':'...'
# print(example_prompt.format(**examples[0]))


prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    # 添加前缀
    prefix="以下是问题解答示例：\n", 
    suffix="问题：{input}",
    # 只声明后缀需要的变量
    input_variables=["input","content"], 
    # 添加示例分隔符 
    example_separator="\n\n" 
)
# 调用时只提供 input 变量,原始需要提供content参数否则会报错
# print(prompt.format(input=" ConversationBufferMemory无法导入?"))
try:
    result = prompt.format(input="ConversationBufferMemory无法导入?",content="解决方案如下:")
    print(result)
except Exception as e:
    print(f"格式化错误: {e}")
    

"""示例选择器exampleselector
使用SemanticSimilarityExampleSelector类
原理：把示例转向量，计算语义相似度匹配
"""
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from Embedding_model.Embeddings_model import BGE_Embed

embeddings = BGE_Embed()
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    # 生成嵌入，用于语义相似的衡量
    embeddings,
    #(向量数据库) 用于存储嵌入和执行相似性搜索的NectorStore类
    Chroma,
    #生成示例数量
    k=1
)
#选择与输入最相似的示例
question="ConversationBufferMemory是什么问题"
seletor_example = example_selector.select_examples({"question":question})
print(f'最相似示例：{question}')
for example in seletor_example:
    print("\\n")
    for k,v in example:
        print(f'{k}:{v}')