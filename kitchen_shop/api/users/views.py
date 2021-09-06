from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from kitchen_shop.api.users.models import Customer
from kitchen_shop.api.users.serializers import (
    CustomerSerializer,
)


class SessionViewSet(ViewSet):
    """Вьюсет пользователей."""

    @action(methods=('get',), detail=False)
    def check_or_create_session(self, request):
        if not request.session or not request.session.session_key:
            request.session.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=('post',), detail=False)
    def create_customer(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        c = Customer(
            first_name=serializer.validated_data.get('first_name'),
            last_name=serializer.validated_data.get('last_name'),
            email=serializer.validated_data.get('email'),
            phone=serializer.validated_data.get('phone'),
            country=serializer.validated_data.get('country'),
            city=serializer.validated_data.get('city'),
            zip=serializer.validated_data.get('zip'),
            sessionid=request.session.session_key
        )
        c.save()
        return Response(status=status.HTTP_200_OK)
