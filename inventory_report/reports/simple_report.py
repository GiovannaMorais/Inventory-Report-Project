from statistics import mode


class SimpleReport:
    def oldest_manufacturing_date_product(products: list):
        return min([product["data_de_fabricacao"] for product in products])

    def closest_expiration_date_product(products: list):
        return min([product["data_de_validade"] for product in products])

    def company_more_products(products: list(dict())):
        return mode([product["nome_da_empresa"] for product in products])

    @classmethod
    def generate(cls, data: list):
        oldest_manufacturing_date = cls.oldest_manufacturing_date_product(data)
        closest_expiration_date = cls.closest_expiration_date_product(data)
        company_biggest_products = cls.company_more_products(data)

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_biggest_products}"
        )
