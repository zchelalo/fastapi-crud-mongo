from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
  title="REST API con FastAPI y MongoDB",
  description="Esto es una REST API simple utilizando FastAPI y MongoDB",
  version="0.0.1",
  openapi_tags=tags_metadata
)

app.include_router(user)