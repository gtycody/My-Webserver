from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
)

POST_TYPE = (
    (0,"article"),
    (1,"code"),
    (2,"photo"),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)

    content = models.TextField()
    
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_type = models.IntegerField(choices=POST_TYPE, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='image_post')
    updated_on = models.DateTimeField(auto_now= True)

    image = models.ImageField(upload_to='image/%Y%m%d/', blank=True)
    
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_type = models.IntegerField(choices=POST_TYPE, default=2)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


    


