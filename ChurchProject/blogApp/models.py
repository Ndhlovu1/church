from django.db import models

from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from django.utils import timezone

#This is our custom manager class
class PublishedBlogManager(models.Manager):

    def get_queryset(self):
        return super(PublishedBlogManager, self).get_queryset().filter(status='published')

# CREATE THE DATABASE FOR OUR BLOG ARTICLES AS A CLASS
class blogDatabase(models.Model):

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft')

    #Declare the default Objects manager
    objects = models.Manager()

    

    #Initialize the new Objects Manager
    publishedBlogs = PublishedBlogManager()

    
    class Meta:
        ordering = ('publish',)

    def __str__(self) :
        return self.title
    
    """
    1. GO INTO THE BLOGAPP FOLDER
    2. LOOK FOR THE Admin.py FILE
    3. ADD THIS CLASS(blogDatabase) INTO THE Admin.py    
    """



