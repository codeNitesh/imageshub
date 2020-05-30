from django.db import models

# Create your models here.

# Create category models
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
        
# Create Image model
class Image(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    image = models.ImageField(upload_to='Images')
    added_date = models.DateTimeField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
