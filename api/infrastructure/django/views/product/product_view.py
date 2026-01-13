from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.application.use_cases.product.create_product import CreateProductUseCase
from api.application.use_cases.product.list_product import ListProductUseCase
from api.infrastructure.database.repositories.category_repository import (
    DjangoCategoryRepository,
)
from api.infrastructure.database.repositories.product_repository import (
    DjangoProductRepository,
)
from api.infrastructure.django.serializers.product_serializer import (
    ProductCreateSerializer,
    ProductSerializer,
)


class ProductView(APIView):
    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = CreateProductUseCase(
            DjangoProductRepository(), DjangoCategoryRepository()
        )
        try:
            product = use_case.execute(**serializer.validated_data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        name = request.query_params.get("name")
        price = request.query_params.get("price")
        category_id = request.query_params.get("category_id")
        brand = request.query_params.get("brand")

        if price:
            price = float(price)
        if category_id:
            category_id = int(category_id)

        use_case = ListProductUseCase(DjangoProductRepository())

        try:
            products = use_case.execute(name, price, category_id, brand)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
