from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.application.use_cases.product.export_product import ExportProductUseCase
from api.infrastructure.database.repositories.product_repository import (
    DjangoProductRepository,
)


class ProductExportView(APIView):
    def get(self, request):
        use_case = ExportProductUseCase(DjangoProductRepository())

        try:
            response = use_case.execute()
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return response
