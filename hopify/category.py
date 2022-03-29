from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='promoteditems',blank=True)
    pricing = models.IntegerField(default= '00')
    
    def __str__(self):
        return str(self.name)