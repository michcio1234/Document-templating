# import jinja_partials
from fastapi.templating import Jinja2Templates
import os.path

_templates_dir = os.path.dirname(__file__)
templates = Jinja2Templates(directory=_templates_dir)
# jinja_partials.register_starlette_extensions(templates)
