from django.db import models

from django.utils import timezone

class Listserv(models.Model):
    title = models.CharField(max_length=200)
    list_id = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Mailing(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    listserv = models.ForeignKey(Listserv, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Source(models.Model):
    brand = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    position = models.FloatField(default=0.0)
    def __str__(self):
        return self.brand

class Topic(models.Model):
    topic = models.CharField(max_length=200)
    def __str__(self):
        return self.topic

class Article(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    summary = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

class Keyword(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=200)
    def __str__(self):
        return self.keywords

class Query(models.Model):
    query = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.query



