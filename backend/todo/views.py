from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsTodoAuthor


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        # one can not use permission_classes with list views
        # so we filter the queryset here
        user = self.request.user
        return Todo.objects.filter(author=user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTodoAuthor,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
