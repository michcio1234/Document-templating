from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from doc_templating.views.doc_fields import router as doc_fields_router

app = FastAPI()
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
app.include_router(doc_fields_router, prefix="")
