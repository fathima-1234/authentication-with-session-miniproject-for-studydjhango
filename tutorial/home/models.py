from django.db import models

# Create your models here.
class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_description= models.TextField()


    def __str__(self):
        return f"{self.about_title} {self.about_description}"



class Places(models.Model):
    places_title = models.CharField(max_length=100)
    places_description= models.TextField()
    places_image = models.ImageField(upload_to='Places')

    
    def __str__(self):
        return f"{self.places_title} {self.places_description} {self. places_image}"




