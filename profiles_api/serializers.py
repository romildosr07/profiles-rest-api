from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializar umm campo nome para testar nossa apiview"""
    name = serializers.CharField(max_length=10)
