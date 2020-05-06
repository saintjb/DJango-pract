from django.db import models


class Topic(models.Model):
    """Themes"""
    text = models.CharField('Текст', max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    text = models.TextField('Текст')
    date_added = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.text[:50]}...'

