from langchain_ollama import ChatOllama, OllamaEmbeddings
from ..base.main import LLMConfig

class OllamaConfig(LLMConfig):
  def __init__(
    self,
    model_name: str = "gemma3:1b",
    embedding_model: str = "llama3",
    base_url: str = "http://localhost:11434",
  ):
    self.model_name = model_name
    self.embedding_model = embedding_model
    self.base_url = base_url

  def get_model(self):
    return ChatOllama(
      model=self.model_name,
      base_url=self.base_url,
    )

  def get_embedding_model(self):
    return OllamaEmbeddings(
      model=self.embedding_model
    )