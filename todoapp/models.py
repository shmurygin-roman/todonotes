from usersapp.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(verbose_name="название", max_length=64, unique=True)
    link = models.CharField(verbose_name="ссылка на репозиторий", max_length=128)
    users = models.ManyToManyField(User, verbose_name="набор пользователей, которые работают с этим проектом")

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField(verbose_name="текст заметки", blank=True)
    created = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="дата обновления", auto_now=True)
    is_active = models.BooleanField(verbose_name="активен", default=True, db_index=True)

    def __str__(self):
        return self.text
