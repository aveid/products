from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

