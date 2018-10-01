from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from django_redis import get_redis_connection




class home(APIView):
    def post(self,request):
        cache.set("key1","value11",200)
        value = cache.get("key1")
        print(value)
        print(cache.ttl("key1"))
        return Response("oooo")