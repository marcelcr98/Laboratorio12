from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer      # add this
from .models import Todo 

class TodoView(viewsets.ModelViewSet):  
  serializer_class = TodoSerializer          # add this
  queryset = Todo.objects.all()     # add this
  

# Create your views here.
