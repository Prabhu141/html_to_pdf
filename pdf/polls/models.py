from django.db import models

# Create your models here.
class Pdf(models.Model):
    link = models.URLField(max_length=255)
    #number = models.PositiveBigIntegerField()
    data = models.FileField(null=False, blank=False,  upload_to='async-kv-table')
    #iso = models.IntegerField()
    #description = models.CharField(max_length=10)
    
    def __str__(self):
        return "%s %s" % (self.link, self.data)
