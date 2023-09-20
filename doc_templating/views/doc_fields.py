from fastapi import APIRouter, Request, Form
from typing import Annotated
from fastapi.responses import StreamingResponse, RedirectResponse
from doc_templating.templates import templates
from doc_templating.viewmodels.doc_fields import DocFieldsViewModel
from doc_templating.services import doc_service, data_service
import logging

log = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
def main(request: Request):
    vm = DocFieldsViewModel(request)
    return templates.TemplateResponse("doc_fields.html", context=vm.dict())


@router.get("/refresh")
def main():
    try:
        data_service.refresh()
    except FileNotFoundError:
        pass
    return RedirectResponse("/", status_code=308)


@router.post("/fill")
def main(request: Request, client_idx: Annotated[int, Form()]):
    vm = DocFieldsViewModel(request, client_idx=client_idx)
    return templates.TemplateResponse("doc_fields.html", context=vm.dict())


@router.post("/submit")
async def submit(request: Request):
    substitutions = await request.form()
    substitutions = doc_service.fill_missing_substitutions(substitutions)
    substitutions = doc_service.preprocess_substitutions(substitutions)
    doc_data = doc_service.substitute_and_stream(substitutions)

    def stream():
        yield from doc_data

    return StreamingResponse(
        stream(),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
