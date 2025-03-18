from django.db import models

class History(models.Model):
    year = models.IntegerField()
    heading = models.CharField(max_length=255)
    short_description = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.heading}"

class Approach(models.Model):
    heading = models.CharField(max_length=255)
    short_description = models.TextField()
    status = models.BooleanField(default=True)
    sequence = models.IntegerField()

    class Meta:
        ordering = ['sequence']  # Orders by sequence

    def __str__(self):
        return self.heading

class Career(models.Model):
    post = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    short_description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.post

class Client(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clients/logos/')
    logo_name = models.CharField(max_length=255)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    person_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='testimonials/images/')
    image_name = models.CharField(max_length=255)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.person_name

class Document(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/')
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
