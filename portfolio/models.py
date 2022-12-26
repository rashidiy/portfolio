from ckeditor.fields import RichTextField
from django.db.models import Model, CharField, URLField, DateTimeField
from django_resized import ResizedImageField


# Create your models here.

class Portfolio(Model):
    image = ResizedImageField(size=[560, 560], crop=['middle', 'center'], upload_to='portfolio')
    title = CharField(max_length=50)
    short_des = CharField(max_length=50)
    project_url = URLField('Project Url')
    created_at = DateTimeField(auto_now_add=True)


class Post(Model):
    image = ResizedImageField(size=[560, 420], crop=['middle', 'center'], upload_to='portfolio')
    title = CharField(max_length=255)
    short_des = CharField(max_length=50)
    long_des = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
