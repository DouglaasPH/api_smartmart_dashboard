from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.application.use_cases.sale.export_sale import ExportSalesUseCase
from api.infrastructure.database.repositories.sale_repository import (
    DjangoSaleRepository,
)


class SaleExportView(APIView):
    def get(self, request):
        use_case = ExportSalesUseCase(DjangoSaleRepository())

        try:
            response = use_case.execute()
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return response
