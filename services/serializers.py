from rest_framework import serializers

from services.models import Category, Service


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = (
            "description", "photo"
        )