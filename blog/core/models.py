from django.db import models
from django.utils import timezone
from django.utils.text import slugify


'''
def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    # post = models.ForeignKey(Preview, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

'''


class Preview(models.Model):
    id_publish = models.IntegerField()
    author = models.CharField(max_length=250)
    resume = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    pushised_data = models.DateTimeField(blank=True, null=True)
    # photo = models.ImageField(upload_to=None, null=True, blank=True)

    def publish(self):
        self.pushised_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tutorial(models.Model):
    id_publish = models.IntegerField()
    author = models.CharField(max_length=250)
    resume = models.TextField()
    title = models.CharField(max_length=250)
    pushised_data = models.DateTimeField(blank=True, null=True)
    # images = models.ManyToManyField(Images)

    def publish(self):
        self.id_publish = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class LifeResume(models.Model):
    author = models.CharField(max_length=250)
    resume = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    pushised_data = models.DateTimeField(blank=True, null=True)
    id_publish = models.IntegerField()

    def publish(self):
        self.pushised_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class LifeContent(models.Model):
    id_publish = models.IntegerField()
    author = models.CharField(max_length=250)
    resume = models.TextField()
    title = models.CharField(max_length=250)
    pushised_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.id_publish = timezone.now()
        self.save()

    def __str__(self):
        return self.title
