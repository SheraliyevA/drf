from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView    
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.http import JsonResponse

class SignUp(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Mavzu(APIView):
    def get(self,request):
        mavzu=Mundarija.objects.all()
        serializer=MunSerializer(mavzu,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=MunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Mashq(APIView):
    def get(self,request):
        theme=Mashqlar.objects.all()
        serializer=MashGetSerializer(theme,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=MashSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(request):
        serializer = MashSerializer(request.user, data=request.DATA, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) 

class Comments(APIView):
    def get(self,request):
        comment=Comment.objects.all()
        serializer=ComGetSerializer(comment,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ComSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MashqDetailView(APIView):
    def get(self,request,pk):
        try:
            mashq=Mashqlar.objects.get(pk=pk)
            ser=MashSerializer(mashq)
            return Response(ser.data)
        except:
            return Response({"xato":"bu id li kitob mavjud emas"})