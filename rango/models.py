from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    NAME_MAX = 128

    name = models.CharField(max_length=NAME_MAX, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Page(models.Model):

    TITLE_MAX = 128

    URL_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX)
    url = models.URLField(max_length = URL_LENGTH)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title