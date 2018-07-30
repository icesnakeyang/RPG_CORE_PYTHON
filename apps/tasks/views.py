from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from .models import Tasks
from .serializers import TaskSerializer


class TaskListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
