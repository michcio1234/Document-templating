from typing import Optional

from .base import ViewModelBase
from fastapi import Request
from doc_templating.services import doc_service, data_service


class DocFieldsViewModel(ViewModelBase):
    def __init__(self, request: Request, client_idx: Optional[int] = None):
        super().__init__(request)
        try:
            self.clients: list[data_service.Client] = data_service.get_client_names()
        except FileNotFoundError:
            self.clients = []
        try:
            self.field_keys: dict[str, doc_service.Field] = doc_service.get_keys()
        except FileNotFoundError:
            self.field_keys = {}
        if client_idx is not None:
            self.clients[client_idx].selected = True
            client_data = data_service.get_single_client_data(client_idx)
            for field, value in client_data.items():
                if field in self.field_keys:
                    self.field_keys[field].default_value = value
