from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def products_stocked_by_company(products: list):
        company_list_str = ""
        company_list = Counter(
            [product["nome_da_empresa"] for product in products]
        )
        companies = dict(company_list)
        for company in companies:
            company_list_str += (
                f"- {company}: {companies[company]}\n")
        return company_list_str

    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        products_stocked = cls.products_stocked_by_company(products)
        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{products_stocked}"
        )
