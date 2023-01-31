import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    try:
        _, file_path, file_type = sys.argv
        result = str

        if file_path.endswith('.csv'):
            result = InventoryRefactor(CsvImporter)
        elif file_path.endswith('.json'):
            result = InventoryRefactor(JsonImporter)
        else:
            result = InventoryRefactor(XmlImporter)

        inventory_report = result.import_data(file_path, file_type)

        print(inventory_report, file=sys.stdout, end="")
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
