from django.db import models, transaction
from django.db.models import F, Max
from django.contrib.auth import get_user_model


class TodoManager(models.Manager):
    """Custom manager for todo ordering"""

    def get_users_todos(self, user):
        """ Return Queryset consisting of users todo-items """
        return Todo.objects.filter(author=user)

    def order(self, todo_object, new_order, user):
        """
        Move an object to a new order position
        and reorder users other todos
        """

        qs = self.get_users_todos(user)

        with transaction.atomic():
            if todo_object.order > int(new_order):
                qs.filter(
                    order__lt=todo_object.order,
                    order__gte=new_order,
                ).exclude(
                    pk=todo_object.pk
                ).update(
                    order=F('order') + 1,
                )
            else:
                qs.filter(
                    order__lte=new_order,
                    order__gt=todo_object.order,
                ).exclude(
                    pk=todo_object.pk,
                ).update(
                    order=F('order') - 1,
                )

            todo_object.order = new_order
            todo_object.save()

    def delete_and_re_order(self, instance, user):
        """
        Delete todo-item and re-order the rest.
        It would be enough to re-order only items after deleted one,
        but by ordering all we can recover if someone sets order
        directly in RDBMS.
        """

        instance.delete()

        todos = self.get_users_todos(user)
        ordered_todos = todos.order_by('order')
        new_order = 1
        # TODO is there a more efficient way to do this?
        with transaction.atomic():
            for todo in ordered_todos:
                todo.order = new_order
                todo.save()
                new_order += 1

        return instance

    def create(self, **kwargs):
        """ Create new todo and place it last """

        instance = self.model(**kwargs)

        with transaction.atomic():
            # Get current max order number
            results = self.all().filter(
                author=instance.author
            ).aggregate(
                Max('order')
            )

            # Increment and use it for new object
            current_order = results['order__max']
            if current_order is None:
                current_order = 0

            value = current_order + 1
            instance.order = value
            instance.save()

        return instance


class Todo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    done_status = models.BooleanField(default=False)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TodoManager()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.author}, {self.text}, {self.order}"
