from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):

    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_path: str, file_type: str):
        self.data.extend(self.importer.import_data(file_path))
        if file_type == 'simples':
            return SimpleReport.generate(self.data)
        if file_type == 'completo':
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
