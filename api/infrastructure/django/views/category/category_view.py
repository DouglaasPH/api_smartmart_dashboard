from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.application.use_cases.category.create_category import CreateCategoryUseCase
from api.application.use_cases.category.list_category import ListCategoryUseCase
from api.infrastructure.database.repositories.category_repository import (
    DjangoCategoryRepository,
)
from api.infrastructure.django.serializers.category_serializer import (
    CategoryCreateSerializer,
    CategorySerializer,
)


class CategoryView(APIView):
    def post(self, request):
        serializer = CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = CreateCategoryUseCase(DjangoCategoryRepository())
        try:
            category = use_case.execute(**serializer.validated_data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CategorySerializer(category)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        use_case = ListCategoryUseCase(DjangoCategoryRepository())
        try:
            categories = use_case.execute()
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
