from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    linkedin = models.URLField(blank=True)
    summary = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Personal Information"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('soft', 'Soft Skills'),
        ('methodology', 'Methodologies'),
        ('programming', 'Programming Languages'),
        ('database', 'Databases'),
        ('tool', 'Tools'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    class Meta:
        ordering = ['category', 'order']

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        ordering = ['order']

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['order']

class Certification(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=10, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
