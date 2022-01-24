from django.shortcuts import render
from rest_framework import generics

class CarCreateView(generics.CreateAPIView):
    serializer_class = ...
