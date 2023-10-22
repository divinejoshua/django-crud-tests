from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title       = models.CharField(max_length = 180)
    body        = models.TextField(blank = False)
    created_at  = models.DateTimeField(auto_now_add= True, auto_now = False, blank = False)

    def __str__(self):
        return self.title