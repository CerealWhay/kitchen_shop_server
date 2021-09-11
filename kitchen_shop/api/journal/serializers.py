from rest_framework import serializers


class PostPreviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False)
    preview_text = serializers.CharField(required=False)
    created = serializers.DateTimeField(required=False)


class FullPostSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    image = serializers.CharField(required=False)
    created = serializers.DateTimeField(required=False)
    main_text = serializers.CharField(required=False)
