import pandas as pd
from doc_templating import config
from dataclasses import dataclass
import logging

log = logging.getLogger(__name__)
clients_data: pd.DataFrame = None


@dataclass
class Client:
    idx: int
    name: str
    selected: bool = False


def _data() -> pd.DataFrame:
    if clients_data is None:
        refresh()
    return clients_data


def refresh():
    global clients_data
    try:
        clients_data = pd.read_excel(config["klienci_plik"].get(str))
    except FileNotFoundError as err:
        log.error(f"Nie znaleziono pliku {err}")
        raise

def get_client_names() -> list[Client]:
    return [
        Client(idx=i, name=item) for i, item in enumerate(_data().iloc[:, 0].values)
    ]


def get_single_client_data(idx: int) -> dict[str, str]:
    return _data().iloc[idx, :].to_dict()
