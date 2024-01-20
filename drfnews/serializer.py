from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','email']

    def create(self,validated_data):
        password=validated_data.pop('password')
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class MunSerializer(ModelSerializer):
    class Meta:
        model=Mundarija
        fields=['id','mavzu']

    def validate(self,attrs):
        mavzu=attrs.get('mavzu')
        if Mundarija.objects.filter(mavzu__contains=mavzu).exists():
            raise serializers.ValidationError({'mavzu':"bunday mavzu mavjud"})
        return attrs
      


class MashSerializer(ModelSerializer):
    class Meta:
        model=Mashqlar
        fields=['id','title','body','user','theme']

    
    def validate(self,attrs):
        theme=attrs.get('theme')
        if Mashqlar.objects.filter(theme__contains=theme).exists():
            raise serializers.ValidationError({'theme':"bunday mavzu mavjud"})
        return attrs
      
class MashGetSerializer(ModelSerializer):
    user=UserSerializer()
    theme=MunSerializer()
    class Meta:
        model=Mashqlar
        fields=['id','title','body','user','theme']

class ComSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','body','user','question']


class ComGetSerializer(ModelSerializer):
    user=UserSerializer()
    question=MashSerializer()
    class Meta:
        model=Comment
        fields=['id','body','user','question']