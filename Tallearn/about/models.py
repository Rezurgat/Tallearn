from django.db import models
from django.utils import timezone


class About(models.Model):
    """ Модель для занесения в базу преподавателя(ФИО, языки, опыт и тд. """
    photo = models.FileField(upload_to='about/')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    link_telegram = models.URLField(default='')
    link_instagram = models.URLField(default='')
    link_vk = models.URLField(default='')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstname}  {self.lastname}'

    class Meta:
        ordering = ['create_at']


class Contact(models.Model):
    """ Модель для создания контактной информации о платформе """
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    link_telegram = models.URLField()
    link_website = models.URLField()


class Feedback(models.Model):
    """ Модель формы фидбека """
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email_or_phone = models.CharField(max_length=100, default='')
    message = models.TextField(max_length=256)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.firstname}  {self.lastname} - ({self.email_or_phone})'

    class Meta:
        ordering = ['create_at']



