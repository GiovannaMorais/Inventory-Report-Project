from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, file_path: str, file_type: str):
        if file_path.endswith('.csv'):
            with open(file_path) as files:
                reader = csv.DictReader(files)
                list_file = list(reader)

        if file_path.endswith('.json'):
            with open(file_path) as files:
                list_file = json.load(files)

        if file_type == 'simples':
            return SimpleReport.generate(list_file)
        if file_type == 'completo':
            return CompleteReport.generate(list_file)
