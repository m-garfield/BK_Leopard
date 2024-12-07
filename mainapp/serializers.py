from rest_framework import serializers
from .models import Galery
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galery
        fields = '__all__'