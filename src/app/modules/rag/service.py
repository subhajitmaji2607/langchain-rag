from src.app.core.llm_config.ollama.config import OllamaConfig


async def data_ingestion():
  pass

def rag_query(user_query: str) -> str:
  """
  Process the user's query and return a response.
  Args:
    user_query (str): The query string provided by the user."""
  # Placeholder logic for processing the query
  try:
    model = OllamaConfig().get_model()
    response = model.invoke(user_query)
    return response.content
  except Exception as e:
    raise Exception(f"Error processing query: {str(e)}")
    