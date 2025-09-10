from django.contrib import admin
from .models import Ads, Category, Condition, Comment, PayType, Location
# Register your models here.

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(PayType)
admin.site.register(Condition)
admin.site.register(Ads)
admin.site.register(Comment)