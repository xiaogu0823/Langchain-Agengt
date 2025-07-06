from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer


# 创建符合langchain标准的词嵌入模型
# 该类需要继承 Embeddings
# 并实现 embed_documents embed_query 方法
class BGE_Embed(Embeddings):
    def __init__(self):
        # 加载 bge-small-zh
        self.embedding = SentenceTransformer(r'C:\Users\Administrator\Desktop\Agent_project\bge-small-zh')

    # 对文档进行词嵌入
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [self.embed_query(text) for text in texts]

    # 对查询语句进行嵌入
    def embed_query(self, text: str) -> list[float]:
        return self.embedding.encode(text).tolist()