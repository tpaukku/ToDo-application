from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'text', 'order')
        model = Todo
