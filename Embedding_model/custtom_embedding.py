from langchain.embeddings import BaseEmbeddings
from transformers import BertTokenizer, BertModel
import torch

class CustomEmbeddingModel(BaseEmbeddings):
    def __init__(self, model_name='bert-base-uncased'):
        """
        初始化自定义词嵌入模型，使用 BERT 作为嵌入模型,可替换其他模型
        :param model_name: BERT 模型（ `bert-base-uncased`）
        """
        # 加载预训练的 BERT 模型和 Tokenizer
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)

    def embed_documents(self, texts):
        """
        将多个文本转换为嵌入向量
        :param texts: 文本列表
        :return: 嵌入向量列表
        """
        embeddings = []
        for text in texts:
            # 使用 tokenizer 对文本进行编码
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
            
            # 获取 BERT 模型的输出（[CLS] token对应的嵌入向量）
            with torch.no_grad():  # 不进行梯度计算
                outputs = self.model(**inputs)
            
            # 获取[CLS] token的输出作为句子的表示
            embeddings.append(outputs.last_hidden_state[:, 0, :].squeeze().cpu().numpy())
        
        return embeddings

    def embed_query(self, query):
        """
        将单个查询文本转换为嵌入向量
        :param query: 查询文本
        :return: 嵌入向量
        """
        inputs = self.tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=512)
        
        # 获取 BERT 模型的输出（[CLS] token对应的嵌入向量）
        with torch.no_grad():  # 不进行梯度计算
            outputs = self.model(**inputs)
        
        # 获取[CLS] token的输出作为查询的表示
        return outputs.last_hidden_state[:, 0, :].squeeze().cpu().numpy()
