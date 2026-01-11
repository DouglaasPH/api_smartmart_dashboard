import csv
import io

from api.domain.entities.sale_entity import Sale


class FakeSaleRepository:
    def list(self):
        return [
            Sale(id=1, product_id=10, date="2026-01-11", quantity=2, total_price=100.0),
            Sale(id=2, product_id=11, date="2026-01-12", quantity=1, total_price=50.0),
        ]


def test_export_sales_usecase():
    repo = FakeSaleRepository()

    output = io.StringIO()
    writer = csv.writer(output)

    # Cabeçalho
    writer.writerow(["id", "product_id", "date", "quantity", "total_price"])

    # Dados
    for sale in repo.list():
        writer.writerow(
            [sale.id, sale.product_id, sale.date, sale.quantity, sale.total_price]
        )

    output.seek(0)
    content = output.read()
    assert "id,product_id,date,quantity,total_price" in content
    assert "1,10,2026-01-11,2,100.0" in content
    assert "2,11,2026-01-12,1,50.0" in content
