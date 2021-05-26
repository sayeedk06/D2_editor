from django.db import models

# Database model for storing text data
class TextData(models.Model):
    text = models.CharField(max_length=1000)
    text_url_id = models.CharField(max_length=100)
    # text_type = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date_created)
        
class TextHist(models.Model):
    prev_text = models.CharField(max_length=100,null=True)
    current_text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.current_text




        
