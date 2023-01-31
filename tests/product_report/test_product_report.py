from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock_product = Product(
        6,
        "Chocolate",
        "Cacau Show",
        "2022-12-31",
        "2022-01-31",
        "CACAU123",
        "Na geladeira",
    )

    mock_relatorio_product = (
        f"O produto {mock_product.nome_do_produto}"
        f" fabricado em {mock_product.data_de_fabricacao}"
        f" por {mock_product.nome_da_empresa} com validade"
        f" até {mock_product.data_de_validade}"
        f" precisa ser armazenado {mock_product.instrucoes_de_armazenamento}."
    )

    assert repr(mock_product) == mock_relatorio_product
