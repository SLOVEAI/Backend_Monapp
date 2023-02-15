from django.http import JsonResponse
from django.forms.models import model_to_dict
from user.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.serializers import UserSerializer


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Server working!🔥🔥🔥"})


@api_view(["GET"])
def all_user(request, *argsm, ** kwargs):
    instance = User.objects.all()
    data = {}
    if instance:
        data = UserSerializer(instance).data
    return Response(data)
