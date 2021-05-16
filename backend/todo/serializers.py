from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    id = serializers.HyperlinkedIdentityField(view_name='todo_detail')
    order = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', 'text', 'order', 'author', 'done_status')
        model = Todo


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'order')
        model = Todo
