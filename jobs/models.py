from django.db import models

class Job(models.Model):
    def __str__(self):
        return self.summary
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)