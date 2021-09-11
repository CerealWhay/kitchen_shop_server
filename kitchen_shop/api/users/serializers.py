from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    zip = serializers.CharField(required=False)


class AppealSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    message = serializers.CharField(required=False)
