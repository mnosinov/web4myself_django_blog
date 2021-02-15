from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='URL тега', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "blog"
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']
