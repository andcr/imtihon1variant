from django.db import models

class TelegramMessage(models.Model):
    sent_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    sender = models.CharField(max_length=255)
