from django.db import models
from clothing.models import ClothingModel
from rest_framework.serializers import ModelSerializer

# Tell REST Framework how to convert cloth into json:
class ClothSerializer(ModelSerializer):
    class Meta:
        model = ClothingModel
        fields = "__all__"