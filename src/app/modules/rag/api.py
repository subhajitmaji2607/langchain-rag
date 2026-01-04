from fastapi import APIRouter, HTTPException, status
from .model import UserQuery, RagResponse
from .service import rag_query as process_rag_query

router = APIRouter(
  prefix="/rag",
  tags=["RAG"]
)

@router.post("/data-ingestion")
async def data_ingestion():
  try:
    return {"message": "This is the RAG module API endpoint."}
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail=str(e)
    )

@router.post("/rag-query", response_model=RagResponse, description="Process a RAG query and return the response.")
async def rag_query(payload: UserQuery):
  try:
    user_query = payload.query
    if not user_query:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Query cannot be empty."
      )
    response = process_rag_query(user_query)
    return {
      "message": "RAG query processed successfully.",
      "data": response
    }
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail=str(e)
    )