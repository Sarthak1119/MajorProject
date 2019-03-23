from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import HttpResponseRedirect
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


class UserCreate(APIView):
    def get(self,request):
        return render(request, 'signup.html')

    def post(self, request, format='json'):

        username = request.data.get('uname')
        email = request.data.get('email')
        password= request.data.get('passw')
        First_Name = request.data.get('fname')
        Last_Name = request.data.get('lname')
        serializer = UserSerializer(data={'first_name':First_Name,'last_name':Last_Name,'username':username, 'email':email,'password':password})
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key

                return HttpResponseRedirect('login/')
            else:
                messages.error(request, serializer.errors)
                return render(request, 'signup.html')

        messages.error(request, serializer.errors)
        return render(request, 'signup.html')


class Loginview(APIView):

    def get(self,request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:

            messages.error(request, 'username or password not correct')
            return render(request, 'registration/login.html')


class HomeView(APIView):

    def get(self,request):
        if request.user.is_authenticated:
            return render(request,'home.html')
        else:
            return render(request,'index.html')








