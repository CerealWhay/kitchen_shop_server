from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from kitchen_shop.api.journal.models import Post
from kitchen_shop.api.journal.serializers import (
    PostPreviewSerializer,
    FullPostSerializer,
)


class JournalViewSet(ViewSet):

    @action(methods=('get',), detail=False)
    def get_posts(self, request):
        posts = Post.objects.all()
        serializer = PostPreviewSerializer(posts, many=True)
        response = serializer.data
        return Response(
            data=response, status=status.HTTP_200_OK,
        )

    @action(methods=('get',), detail=False)
    def get_selected_post(self, request):
        post = get_object_or_404(Post, id=request.query_params.get('id'))
        serializer = FullPostSerializer(post)
        response = serializer.data

        return Response(
            data=response, status=status.HTTP_200_OK
        )