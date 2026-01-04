from abc import ABC, abstractmethod
from typing import Any


class LLMConfig(ABC):
  """
  Base configuration for all LLM providers.
  Child classes MUST implement all abstract methods.
  """

  @abstractmethod
  def get_model(self) -> Any:
    """
    Return a LangChain LLM / Chat Model instance
    """
    pass

  @abstractmethod
  def get_embedding_model(self) -> Any:
    """
    Return a LangChain Embeddings instance
    """
    pass
