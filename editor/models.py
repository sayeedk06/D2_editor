from django.db import models

# Database model for storing text data
class TextData(models.Model):
    text = models.CharField(max_length=1000)
    text_url_id = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date_created)