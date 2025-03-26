
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the date and time when the record is created

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"
