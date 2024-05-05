from django.db import models

# Create your models here.

class ChatConversation(models.Model):
    #userid = models.IntegerField(unique=True)
    session_id = models.CharField(max_length=1000)
    bot_message = models.CharField(max_length=10000,null=True)
    user_message = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically record creation time
    class meta:
        ordering = ['-timestamp','-session_id']

    def __str__(self):
        return f"{self.timestamp}" + " - " + f"{self.session_id}"


class newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    class meta:
        ordering = ['name']
    def __str__(self):
        return f"{self.name}" + " - " + f"{self.email}"