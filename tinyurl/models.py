from django.db import models

class TinyURL(models.Model):
    long_url = models.CharField(max_length=500)
    description = models.CharField(max_length=50)
    short_url = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
