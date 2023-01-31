from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if file_path.endswith(".xml"):
            with open(file_path) as files:
                reader = files.read()
                list_file = xmltodict.parse(reader)["dataset"]["record"]
            return list_file

        raise ValueError("Arquivo inválido")
