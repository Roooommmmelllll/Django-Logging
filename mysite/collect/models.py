from django.db import models

# Create your models here.

class Query(models.Model):
    query_text = models.CharField(max_length=200)
    tally = models.IntegerField(default=0)

    def __st__(self):
        return self.query_text
