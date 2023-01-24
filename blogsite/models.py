from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



class Blog(models.Model):
    #thumb = models.ImageField(default=None,upload_to = "thums/",)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.title + '|' + str(self.author) +"| " +str(self.id)

    def get_absolute_url(self):
        return reverse("index")