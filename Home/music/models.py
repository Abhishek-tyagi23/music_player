from django.db import models


# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=255)         
    artist = models.CharField(max_length=255, default='Unknown Artist')        
    # audio = models.FileField(upload_to='songs/')  
    audio = models.FileField(upload_to='audio_files/') 
    thumbnail = models.ImageField(upload_to='thumbnails/')


    class Meta:
        db_table = 'Card'

    def __str__(self):
        return self.title