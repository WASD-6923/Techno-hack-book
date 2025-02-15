from django.db import models
from django.urls import reverse

class Soldat(models.Model):
    name = models.CharField(max_length=20,unique=True)
    slug = models.SlugField(max_length=20,unique=True)
    
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Солдат'

    def __str__(self):
        return self.name
    

class Geroy(models.Model):
    category = models.ForeignKey(Soldat,related_name='geroys',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='geroy/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    age = models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['name']
        indexes = [
            models.Index(fields=['id','slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),

        ]
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:geroy_detail",args=[self.slug])
    
        
# Create your models here.
