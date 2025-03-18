from django.db import models

# News Category Model
class NewsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# News Model
class News(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='news/images/')
    image_name = models.CharField(max_length=255)
    inner_image = models.ImageField(upload_to='news/inner_images/', blank=True, null=True)
    inner_image_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/images/')
    image_name = models.CharField(max_length=255)
    description = models.TextField()
    exhibition_name = models.CharField(max_length=255)
    booth_number = models.CharField(max_length=50)
    venue = models.CharField(max_length=255)
    time = models.CharField(max_length=100)
    hall_number = models.CharField(max_length=50)

    def __str__(self):
        return self.title
