from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Staff
from django.contrib.auth.models import User
from .serializers import StaffSerializer
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])
def signUp(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(['POST'])
# def logIn(request):
#     username = request.data['user']['username']
#     password = request.data['user']['password']
#     user = User.objects.get(username=username, password=password)
#     print(user)
#     staff = Staff.objects.get(user=user)
#     serializer = StaffSerializer(staff, many=False)
#     if Staff.objects.filter(username=username, password=password).exists():
#         token = Token.objects.create()
#     token = "user doesnt exist"
#     return Response(token)


# {
#     "user" : {
#         "username":"amelie",
#         "email":"amelie@gmail.com",
#         "password":"12345"
#     },
#     "name":"Amelie"
# }

# {
#     "user" : {
#             "username":"amelie",
#             "password":"12345"
#         }
# }

