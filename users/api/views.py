from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
from users.api.serializers import UserSerializer
from users.models import User
from rest_framework.renderers import JSONRenderer

class UserListApi(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
  
        return Response(serializer.data)
    
    def post(self, request):
        return Response("Todo ok")