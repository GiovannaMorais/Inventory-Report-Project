from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.endswith(".json"):
            with open(file_path) as files:
                list_file = json.load(files)
            return list_file

        raise ValueError("Arquivo inválido")
