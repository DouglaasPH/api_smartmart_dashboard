import csv
import io

from django.http import JsonResponse

from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.application.use_cases.product.create_product import CreateProductUseCase
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


class ProductImportView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return JsonResponse({"error": "CSV file not provided"}, status=400)

        decoded_file = file.read().decode("utf-8")
        reader = csv.DictReader(io.StringIO(decoded_file))

        response = []

        use_case = CreateProductUseCase(
            DjangoProductRepository(), DjangoCategoryRepository()
        )

        for row in reader:
            try:
                category_id = int(row.get("category_id"))
                name = row.get("name")
                description = row.get("description")
                price = float(row.get("price"))
                brand = row.get("brand")

                serializer = ProductCreateSerializer(
                    data={
                        "category_id": category_id,
                        "name": name,
                        "description": description,
                        "price": price,
                        "brand": brand,
                    }
                )
                serializer.is_valid(raise_exception=True)

                product = use_case.execute(**serializer.validated_data)
                response.append(product)
            except ValueError:
                continue

        serializer = ProductSerializer(response, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
