from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer, OrderSerializer
from .permissions import IsTodoAuthor


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        # One can not use permission_classes with list views
        # so we filter the queryset here.
        # User can only see her own todos
        user = self.request.user
        return Todo.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTodoAuthor,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_destroy(self, instance):
        Todo.objects.delete_and_re_order(instance, self.request.user)


class TodoOrder(APIView):
    serializer_class = OrderSerializer

    def post(self, request, pk):
        user = request.user
        todo_object = Todo.objects.get(id=pk)
        new_order = request.data.get('order')

        # User does not own todo-item
        if todo_object.author != user:
            return Response(
                data={'detail':
                      'You do not have permission to perform this action.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        # No order in request
        if new_order is None or new_order == '':
            return Response(
                data={'detail': 'No order given'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Order is below one
        if int(new_order) < 1:
            return Response(
                data={'detail': 'Order cannot be zero or below'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        todo_object_json = OrderSerializer(todo_object, many=False)

        # Call for Todo model manager to reorder todos
        Todo.objects.order(todo_object, new_order, user)

        return Response(todo_object_json.data)
