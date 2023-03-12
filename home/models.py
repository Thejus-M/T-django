from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_icon = models.CharField(max_length=10)
    
    def __str__(self):
        return self.tag_name
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    project_pic = models.ImageField(upload_to='images')
    description = models.TextField(max_length=1000)
    tag=models.ManyToManyField(Tag)
    read_more_url = models.URLField(max_length = 200)
    website_url = models.URLField(max_length = 200)
    
    
    def __str__(self):
        return self.title
    