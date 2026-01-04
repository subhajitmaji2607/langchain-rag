from pydantic import BaseModel, Field

class UserQuery(BaseModel):
  query: str = Field(min_length=1, max_length=500, description="The user's query string.")

class RagResponse(BaseModel):
  message: str
  data: str