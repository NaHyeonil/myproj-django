from rest_framework import serializers
from hotdeal.models import Hotdeal


class HotdealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotdeal
        fields = "__all__"