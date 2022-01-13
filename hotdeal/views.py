from rest_framework.viewsets import ModelViewSet
from hotdeal.models import Hotdeal
from hotdeal.serializers import HotdealSerializer


class HotdealViewSet(ModelViewSet):
    queryset = Hotdeal.objects.all()
    serializer_class = HotdealSerializer
