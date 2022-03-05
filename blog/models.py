from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# models provide the basis for our posts

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    image = CloudinaryField('image', default='https://res.cloudinary.com/ddxxrzq7g/image/upload/v1646105774/pink_flowers_pskkjx.jpg')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def like_count(self):
        return self.likes.count()