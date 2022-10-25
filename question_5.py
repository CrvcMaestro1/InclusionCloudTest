import json
import logging
from datetime import datetime
from typing import List, Dict, Optional

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
logging.basicConfig(level="INFO")
logger = logging.getLogger("question5")


class InvoiceManager:

    def __init__(self, fixtures_file: str) -> None:
        self.fixtures_file = fixtures_file

    def _get_json(self):
        data = dict()
        with open(self.fixtures_file) as jf:
            data = json.load(jf)
        return data

    @staticmethod
    def _write_json(fixtures_file: str, data: Dict) -> None:
        with open(fixtures_file, "w") as jf:
            json.dump(data, jf)

    def build_file_name(self, text: str) -> str:
        split = self.fixtures_file.split(".")
        return f"{split[0]}_{text}.{split[1]}"

    def get_payee_id(self) -> str:
        data = self._get_json()
        payee = data.get("payee")
        payee_id = payee.get("id")
        return payee_id

    def filter_invoices_by_text(self, text: str) -> List[str]:
        data = self._get_json()
        invoices = data.get("invoiceIds")
        filtered_invoices = [invoice for invoice in invoices if text in invoice]
        return filtered_invoices

    def change_dateformat(self, field: str) -> Optional[str]:
        data = self._get_json()
        integer_timestamp = data.get(field, None)
        if integer_timestamp is not None:
            if isinstance(integer_timestamp, int):
                datetime_obj = datetime.fromtimestamp(integer_timestamp / 1e3)
                data[field] = datetime_obj.strftime(DATETIME_FORMAT)
                filename = self.build_file_name(field)
                self._write_json(filename, data)
                logger.info("File successfully written with document changes")
                return filename
            else:
                logger.error("The date was not the type of data expected")
        else:
            logger.error("The date is empty")
        return None
