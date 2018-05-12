from django.db import models
from django.contrib.auth.models import User


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Photo(CommonInfo):
    image = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=256, blank=True, null=True)


    def __str__(self):
        return f'{self.id} | {self.image}'

    class Meta:
        verbose_name_plural = 'Upload Photos'
        ordering = ('created',)


class Category(CommonInfo):
    name = models.CharField(max_length=32, blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.name}'

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(CommonInfo):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f'{self.id} | {self.name}'

    class Meta:
        verbose_name_plural = 'Tags to Photos'


class Comment(CommonInfo):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512, blank=True, null=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return f'{self.id} | {self.user}'

    class Meta:
        verbose_name_plural = 'Comments to Photos'


class Voice(CommonInfo):
    photo = models.OneToOneField(Photo, on_delete=models.CASCADE)
    counter = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.id} | {self.counter}'
