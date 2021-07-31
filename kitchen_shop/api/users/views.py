from django.forms import model_to_dict
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from kitchen_shop.api.users.models import Customer


class BaseAuthViewSet(ViewSet):
    """Вьюсет пользователей."""

    @action(methods=('get',), detail=False)
    def create_session(self, request):
        print(request.session.session_key)
        if not request.session or not request.session.session_key:
            request.session.save()
            c = Customer(sessionid=request.session.session_key)
            c.save()
        print(request.session.session_key)
        return Response(status=status.HTTP_200_OK)
