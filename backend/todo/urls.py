from django.urls import path
from .views import TodoList, TodoDetail, TodoOrder

urlpatterns = [
    path('<int:pk>/order/', TodoOrder.as_view(), name='todo_order'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
    path('', TodoList.as_view(), name='todo_list')
]
