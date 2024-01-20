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



# def detail(request,pk):
#     poll=get_object_or_404(Mashqlar,pk=pk)
#     context={"result":{
#             'question':poll.title,
#             'question_body':poll.body,
#             'create':poll.created
#         }}
#     return JsonResponse(data)
