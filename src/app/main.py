from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.app.modules.rag.api import router as rag_router

app = FastAPI(
  title="Langchain RAG API",
  description="API for Retrieval-Augmented Generation using Langchain",
  version="1.0.0",
  root_path="/api/v1"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
  validation_errors = []
  for error in exc.errors():
    validation_errors.append({
      "loc": error.get("loc", []),
      "msg": error.get("msg", ""),
      "type": error.get("type", "")
    })
  return JSONResponse(
    status_code=422,
    content={
      "message": "validation error",
      "errors": validation_errors
    },
  )

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}


# Include additional route definitions and logic here
app.include_router(rag_router)