from django.forms import model_to_dict
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from kitchen_shop.api.users.logic.auth import Authenticator
from kitchen_shop.api.users.logic.register import Registerer
from kitchen_shop.api.users.serializers import (
    RegisterSerializer,
    LoginSerializer,
    LoginResponseSerializer,
    AddressSerializer,
    UserSerializer,
)


class BaseAuthViewSet(ViewSet):
    """Вьюсет пользователей."""

    permission_classes = (permissions.AllowAny,)

    @action(methods=('post',), detail=False)
    def register(self, request):
        """Эндпоинт на регистрацию пользователя."""
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Registerer.register(serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

    @action(methods=('post',), detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = Authenticator.login(
            serializer.validated_data.get('username'),
            serializer.validated_data.get('password'),
            request
        )
        serializer = LoginResponseSerializer(
            data=dict(
                token=token,
                user=model_to_dict(user),
            )
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )

    @action(methods=('post',), detail=False)
    def logout(self, request):
        """Логаут пользователя."""
        if not request.user.is_authenticated or request.auth is None:
            response = Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            Authenticator.logout(request.auth.key)
            response = Response(status=status.HTTP_200_OK)
        return response


class UserDataViewSet(ViewSet):
    """Вьюсет пользователей."""

    permission_classes = (permissions.AllowAny,)

    @action(methods=('post',), detail=False)
    def set_address(self, request):
        user = request.user
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        country = serializer.validated_data.get('country'),
        city = serializer.validated_data.get('city'),
        zip = serializer.validated_data.get('zip'),
        phone = serializer.validated_data.get('phone'),

        user.country = country[0]
        user.city = city[0]
        user.zip = zip[0]
        user.phone = phone[0]
        user.save()

        return Response(status=status.HTTP_200_OK)

    @action(methods=('get',), detail=False)
    def get_address(self, request):
        user = request.user

        serializer = AddressSerializer(
            data=model_to_dict(user)
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )

    @action(methods=('post',), detail=False)
    def change_personal_data(self, request):
        user = request.user

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        first_name = serializer.validated_data.get('first_name'),
        last_name = serializer.validated_data.get('last_name'),
        email = serializer.validated_data.get('email'),

        user.first_name = first_name[0]
        user.last_name = last_name[0]
        user.email = email[0]
        user.save()

        serializer = LoginResponseSerializer(
            data=dict(
                user=model_to_dict(user)
            )
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )
