from django.db import models
from django.contrib.auth import get_user_model


class Todo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    done_status = models.BooleanField(default=False)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}, {self.text}"
