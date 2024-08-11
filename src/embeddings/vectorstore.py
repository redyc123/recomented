from typing import List
from embeddings.model import model
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.documents import Document
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import EmbeddingsFilter


class VecStore:
    chroma: Chroma = None

    def __init__(
        self,
        collection_name: str,
        docs: List[Document] = []
    ) -> None:
        self.collection_name = collection_name
        self.add_documents(docs)

    def add_documents(self, docs: List[Document]):
        self.chroma = Chroma(self.collection_name, embedding_function=model)
        self.chroma.from_documents(
            collection_name=self.collection_name,
            documents=docs,
            embedding=model
        )

    def search(self, query: str) -> List[Document]:
        return self.chroma.as_retriever().invoke(query)

    def rerank(self, query: str) -> List[Document]:
        embeddings_filter = EmbeddingsFilter(
            embeddings=model,
            k=None,
            similarity_threshold=0.5
        )

        compression_retriever = ContextualCompressionRetriever(
            base_compressor=embeddings_filter,
            base_retriever=self.chroma.as_retriever()
        )

        return compression_retriever.get_relevant_documents(query)
