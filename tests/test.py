import pytest
from pathlib import Path
from docx import Document

from doc_templating.services.doc_service import get_keys, substitute


@pytest.fixture()
def template_path():
    return Path(__file__).parent / "assets" / "template.docx"


@pytest.fixture()
def doc(template_path):
    return Document(template_path)


def test_get_keys(doc):
    keys = get_keys(doc)
    print(keys)
    assert len(keys) > 5
    assert keys["stawka za wizytę"] == "70"


def test_substitute(doc, template_path):
    subs = dict(
        nazwiskoNarzednik="Januszem Kowalskim",
        kot="Mruczek",
        liczbaWizyt="5",
        stawkaZaWizyte="70",
    )
    substitute(subs, doc)
    doc.save(template_path.parent / "modified.docx")
