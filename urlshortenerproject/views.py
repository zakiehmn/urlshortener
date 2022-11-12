from signal import valid_signals
from sqlite3 import adapt
from termios import VSTART
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Staff, Shortener
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .serializers import StaffSerializer, LoginSerializer, ShortenerSerializer
from rest_framework.authtoken.models import Token
from django.http import HttpResponseRedirect, Http404
from .utils import create_random_slug


# Create your views here.

@api_view(['POST'])
def signUp(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def logIn(request):
    username = request.data['user']['username']
    password = request.data['user']['password']
    user = authenticate(username=username, password=password)
    print(user)
    staff = Staff.objects.get(user=user)
    if user :
        login(request, user)
        serializer = LoginSerializer(staff, many=False)
    else:
        print("!!!!!!!!!!")

    return Response(serializer.data)


@api_view(['GET'])
def unauthorized(request):
    return Response({'error': 'Token does not exist'}, status=401)

@api_view(['POST'])
@login_required()
def create_url_shortener(request):
    print(request.data)
    user = request.user
    staff = Staff.objects.get(user=user)
    link = request.data['link']
    if 'slug' in request.data :
        slug = request.data['slug']
    else:
        slug = create_random_slug()
    shortener = Shortener.objects.create(long_url=link, short_url=request.build_absolute_uri('/')+slug, user=user)
    # print(request.build_absolute_uri('/'))
    serializer = ShortenerSerializer(shortener, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def redirect_url_view(request, shortened_part):
    print("1")
    try:
        shortener  = Shortener.objects.get(short_url=request.build_absolute_uri('/')+shortened_part)
        print(shortener)
        print(shortener.long_url)
        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404('Sorry this link is broken :(')




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

# {
# 	"link" : ""
# }