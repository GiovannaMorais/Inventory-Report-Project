from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.endswith(".csv"):
            with open(file_path) as files:
                reader = csv.DictReader(files)
                list_file = list(reader)
            return list_file

        raise ValueError("Arquivo inválido")
