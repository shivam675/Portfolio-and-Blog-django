from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images/',  blank=True)
    url = models.URLField(blank=True)

    type = [
    ('user-interface', 'Robotics'),
    ('branding', 'Web',),
    ('mockup','Microcontroller',),
    ('ui','Photograpy',),
    ]
    cat = models.CharField(max_length=20, choices=type, default='ui')



    def __str__(self):
        return self.title


class contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_adress = models.EmailField(max_length = 254)
    message = models.TextField()
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Certificate(models.Model):
    """docstring for Certificates."""
    certificate_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/',  blank=True)
    pdf = models.FileField(upload_to='portfolio/pdf')

    def __str__(self):
        return self.certificate_title
