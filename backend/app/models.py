from django.db import models

class User(models.Model):
    """
        Пользователь
    """
    full_name = models.CharField(max_length=300, null=False, unique=True)
    position_name = models.CharField(max_length=300, null=False)


class Message(models.Model):
    """
        Сообщение 
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    message_text = models.TextField(null=False)
    dttm = models.DateTimeField(null=False)
