from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from doc_templating.views.doc_fields import router as doc_fields_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="doc_templating/static"), name="static")
app.include_router(doc_fields_router, prefix="")
