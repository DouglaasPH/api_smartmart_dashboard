from django.urls import path

from api.infrastructure.django.views.category.category_view import CategoryView
from api.infrastructure.django.views.product.export_product_view import (
    ProductExportView,
)
from api.infrastructure.django.views.product.import_product_view import (
    ProductImportView,
)
from api.infrastructure.django.views.product.product_view import ProductView
from api.infrastructure.django.views.sale.export_sale_view import SaleExportView
from api.infrastructure.django.views.sale.sale_view import SaleView

urlpatterns = [
    # Categories
    path("categories/", CategoryView.as_view()),
    # Products
    path("products/", ProductView.as_view()),
    path("products/export/", ProductExportView.as_view()),
    path("products/import/", ProductImportView.as_view()),
    # Sales
    path("sales/", SaleView.as_view()),
    path("sales/<int:id>/", SaleView.as_view()),
    path("sales/export/", SaleExportView.as_view()),
]
