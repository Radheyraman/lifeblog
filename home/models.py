from django.db import models

# Create your models here.
class Post(models.Model):
    Pno=models.AutoField(primary_key=True)
    slug=models.CharField(max_length=25)
    Title=models.CharField(max_length=25)
    contents=models.TextField()
    author=models.CharField(max_length=13)
    timeDate=models.DateTimeField(blank=True)
    images=models.ImageField(upload_to="static/images",default="")

    def __str__(self):
        return self.Title