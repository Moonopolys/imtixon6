from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shaxar"
        verbose_name_plural = "Shaxarlar"


class PayType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "To'lo'v"
        verbose_name_plural = "To'lo'vlar"


class Condition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Xolat"
        verbose_name_plural = "Xolatlar"


class Ads(models.Model):
    address = models.TextField(null=True, blank=True, verbose_name="Manzili")
    title = models.CharField(max_length=250, verbose_name="Maqola nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Maqola matni")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    item = models.CharField(max_length=155, verbose_name="Maxsulot nomi")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Rasmi")
    video = models.FileField(upload_to="media/", null=True, blank=True, verbose_name="Videosi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    price = models.IntegerField(default=0, verbose_name="Narxi")
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, verbose_name="Maxsulot xolati")
    pay_type = models.ForeignKey(PayType, on_delete=models.CASCADE, verbose_name="To'lo'v turi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Bo'limi")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Shaxar")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"
        ordering = ['-created']



class Comment(models.Model):
    text = models.CharField(max_length=500, verbose_name="Matni")
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE, verbose_name="Maqola")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Avtor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yozilgan vaqti")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ["-created"]