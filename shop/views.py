from django.views.generic import ListView
from rest_framework import viewsets
from shop.models import Review
from shop.serializers import ReviewSerializer


review_list = ListView.as_view(model=Review)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer