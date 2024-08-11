from langchain_community.embeddings.huggingface_hub import HuggingFaceHubEmbeddings
import os

model = HuggingFaceHubEmbeddings(model=os.environ["EMB_URL"])
