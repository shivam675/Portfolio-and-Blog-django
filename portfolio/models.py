from django.db import models
from blog.models import Blog

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
    ('mis', 'Miscellaneous')
    ]
    cat = models.CharField(max_length=20, choices=type, default='ui')
    post = models.ForeignKey(Blog, null=True, default=None, on_delete = models.CASCADE, related_name ='project_blog')

    date_of_completion = models.DateField()
    # status = models.CharField(max_length=20, choices=type, default='ui')

    def __str__(self):
        return self.title


# class projectBlog(models.Model):




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

    type = [
    ('user-interface', 'Robotics'),
    ('branding', 'Web',),
    ('mockup','IOT',),
    ('ui','AI',),
    ('mis', 'Miscellaneous'),
    ('par', 'Participation'),
    ]

    pn_list = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    ]


    priority_number = models.IntegerField(choices=pn_list)
    catc = models.CharField(max_length=20, choices=type, default='ui')
    image = models.ImageField(upload_to='portfolio/images/',  blank=True)
    pdf = models.FileField(upload_to='portfolio/pdf')
    date_of_completion = models.DateField()


    def __str__(self):
        return self.certificate_title
