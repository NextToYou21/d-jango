from django.db import models


# Create your models here.
class EgModel(models.Model):
    string_field = models.CharField(max_length=100)
    textarea = models.TextField()
    integer = models.IntegerField()
    floating_number = models.FloatField()
    date_filed = models.DateField()
    image_filed = models.ImageField(upload_to="images")
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    Image=models.ImageField(upload_to="images")
    date=models.DateField()
    Blog_number= models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title
class comment(models.Model):
    text=models.TextField()