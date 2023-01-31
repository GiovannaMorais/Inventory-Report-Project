from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import pytest

VERMELHO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[36m"
RST = "\033[0m"


@pytest.fixture
def company_product_inventory():
    mock_inventory = [
        {
            "id": 1,
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target",
            "data_de_fabricacao": "2023-10-11",
            "data_de_validade": "2023-11-01",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 2",
        },
        {
            "id": 2,
            "nome_do_produto": "Norepinephrine Bitartrate",
            "nome_da_empresa": "Cantrell Drug Company",
            "data_de_fabricacao": "2023-09-11",
            "data_de_validade": "2023-11-20",
            "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
            "instrucoes_de_armazenamento": "instrucao 4",
        },
    ]
    return mock_inventory


def test_decorar_relatorio(company_product_inventory):
    result = (
        f"{VERDE}Data de fabricação mais antiga:{RST} {AZUL}2023-09-11{RST}\n"
        f"{VERDE}Data de validade mais próxima:{RST} {AZUL}2023-11-01{RST}\n"
        f"{VERDE}Empresa com mais produtos:{RST} {VERMELHO}Target{RST}"
    )

    assert result in ColoredReport(SimpleReport).generate(
        company_product_inventory
    )
    assert result in ColoredReport(CompleteReport).generate(
        company_product_inventory
    )
