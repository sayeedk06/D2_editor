from django.db import models

# Create your models here.
class TextData(models.Model):
    text = models.CharField(max_length=1000)
    text_url_id = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date_created)