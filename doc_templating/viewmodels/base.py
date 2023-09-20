from typing import Optional

from fastapi import Request


class ViewModelBase:
    def __init__(self, request: Request):
        self.request = request
        self.is_htmx_request = "HX-Request" in self.request.headers
        self.error: Optional[int] = None

    def dict(self):
        return self.__dict__
