from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Staff
from .serializers import StaffSerializer

# Create your views here.

@api_view(['POST'])
def signUp(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    print(serializer.data)
    return Response(serializer.data)



# {
#     "user" : {
#         "username":"amelie",
#         "email":"amelie@gmail.com",
#         "password":"12345"
#     },
#     "name":"Amelie"
# }