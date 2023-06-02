from django.db import models

# Create your models here.
# we created a class named songs in order to give the functioning of the app thats why this class is in models.py 
class Songs(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)
    

    def __str__(self) -> str:
        return "{} - {}" .format(self.title, self.artist)
