from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章内容")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="发布日期")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"

