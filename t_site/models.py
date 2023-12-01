from django.db import models


# Create your models here.

class Services(models.Model):
    tittle = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    icon = models.ImageField(upload_to='/icons', blank=False)

    class Meta:
        verbose_name_plural = 'Services'
        unique_together = ['id', 'slug']

    def __str__(self):
        return f"{self.tittle}"


class Portfolio(models.Model):
    tittle = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    image = models.ImageField(upload_to='/images', blank=False)

    class Meta:
        verbose_name_plural = 'Portfolio'
        unique_together = ['id', 'slug']

    def __str__(self):
        return f"{self.tittle}"


class About(models.Model):
    tittle = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    image = models.ImageField(upload_to='/images', blank=False)

    class Meta:
        verbose_name_plural = 'About'
        unique_together = ['id', 'slug']

    def __str__(self):
        return f"{self.tittle}"


class Team(models.Model):
    tittle = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='/team_images', blank=False)

    class Meta:
        verbose_name_plural = 'Team'

    def __str__(self):
        return f"{self.tittle}"


class ContactUs(models.Model):
    name = models.CharField(blank=True)
    email = models.CharField(blank=True)
    phone = models.PositiveSmallIntegerField(blank=True)
    message = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'ContactUS'

    def __str__(self):
        return f"{self.name}"