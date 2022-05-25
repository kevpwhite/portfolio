from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Form"

    def __str__(self):
        return self.name + "-" +  self.email
