from inventory_report.inventory.product import Product


def test_cria_produto():
    mock_product = Product(
        6,
        "Chocolate",
        "Cacau Show",
        "2022-12-31",
        "2022-01-31",
        "CACAU123",
        "Colocar na geladeira"
    )

    assert mock_product.id == 6
    assert mock_product.nome_do_produto == "Chocolate"
    assert mock_product.nome_da_empresa == "Cacau Show"
    assert mock_product.data_de_fabricacao == "2022-12-31"
    assert mock_product.data_de_validade == "2022-01-31"
    assert mock_product.numero_de_serie == "CACAU123"
    assert mock_product.instrucoes_de_armazenamento == "Colocar na geladeira"
