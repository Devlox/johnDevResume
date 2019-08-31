from django.db import models
from django.contrib.auth import get_user_model
from johnresume.utils import unique_slug_generator
from johnresume.utils import category_slug_generator
from django.db.models.signals import pre_save

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    cat_slug = models.SlugField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
def cat_slug_generator(sender, instance, *args, **kwargs):
    if not instance.cat_slug:
        instance.cat_slug = category_slug_generator(instance)

pre_save.connect(cat_slug_generator, sender=Category)


class Post(models.Model):
    title = models.CharField(max_length=100)
    title_def = models.CharField(max_length=150)

    slug = models.SlugField(max_length=500, null=True, blank=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
