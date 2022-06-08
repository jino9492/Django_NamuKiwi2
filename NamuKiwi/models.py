from django.db import models

class PageData(models.Model):
    subject = models.CharField(max_length=200, primary_key=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.subject

# Create your models here.
