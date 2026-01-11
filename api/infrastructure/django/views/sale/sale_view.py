from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.application.use_cases.sale.list_sales import ListSalesUseCase
from api.application.use_cases.sale.update_sale import UpdateSaleUseCase
from api.infrastructure.database.repositories.sale_repository import (
    DjangoSaleRepository,
)
from api.infrastructure.django.serializers.sale_serializer import (
    SaleListSerializer,
    SaleUpdateSerializer,
)


class SaleView(APIView):
    def get(self, request):
        use_case = ListSalesUseCase(DjangoSaleRepository())

        try:
            sales = use_case.execute()
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SaleListSerializer(sales, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        serializer = SaleUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = UpdateSaleUseCase(DjangoSaleRepository())

        try:
            sale = use_case.execute(id=id, **serializer.validated_data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SaleUpdateSerializer(sale)

        return Response(serializer.data, status=status.HTTP_200_OK)
