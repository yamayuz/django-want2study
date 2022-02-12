from django.db import models

class studyModel(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    finishFlg = models.BooleanField()
    created = models.DateTimeField()
    user = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
