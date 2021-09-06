from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class CartViewSet(ViewSet):

    @action(methods=('post',), detail=False)
    def send_cart(self, request):
        response = []
        return Response(
            data=response, status=status.HTTP_200_OK,
        )
