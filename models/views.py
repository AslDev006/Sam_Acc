from django.http import Http404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class ContactCreateView(APIView):
    def post(self, request, format=None):
        serializer = Contact_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalledContactView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        called = Contact_Model.objects.filter(called="Bog'lanildi")
        serializer = Contact_Serializer(called, many=True)
        return Response(serializer.data)

class UnCalledContactView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        called = Contact_Model.objects.filter(called="Bog'lanilmadi")
        serializer = Contact_Serializer(called, many=True)
        return Response(serializer.data)

class AllContactView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        service = Contact_Model.objects.all()
        serializer = Contact_Serializer(service, many=True)
        return Response(serializer.data)

class ContactDetailView(APIView):
    """
    Retrieve, update or delete a transformer instance
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Contact_Model.objects.get(pk=pk)
        except Contact_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct,
                                               data=request.data,
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            conatct = self.get_object(pk)
            conatct.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)