from django.db import models

# Industries Model
class Industry(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='industries/images/')
    image_name = models.CharField(max_length=255)
    coming_soon = models.BooleanField(default=False)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Certification Category Model
class CertificationCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Certification Model
class Certification(models.Model):
    category = models.ForeignKey(CertificationCategory, on_delete=models.CASCADE, related_name="certifications")
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='certifications/files/')
    image = models.ImageField(upload_to='certifications/images/')
    image_name = models.CharField(max_length=255)
    coming_soon = models.BooleanField(default=False)
    downloader_info = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Download Category Model
class DownloadCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Download Model
class Download(models.Model):
    category = models.ForeignKey(DownloadCategory, on_delete=models.CASCADE, related_name="downloads")
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='downloads/files/')
    image = models.ImageField(upload_to='downloads/images/')
    image_name = models.CharField(max_length=255)
    coming_soon = models.BooleanField(default=False)
    downloader_info = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Distributor Model
class Distributor(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.company_name
