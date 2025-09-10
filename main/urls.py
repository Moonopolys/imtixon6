from django.urls import path

from .views import (home, ads_by_category, ads_detail, save_ads, save_comment,
                    update_ads, delete_ads)

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', ads_by_category, name="ads_by_category"),
    path('ads/add/', save_ads, name="ad_ads"),
    path('ads/<int:pk>/', ads_detail, name="ads_detail"),
    path('ads/<int:pk>/update/', update_ads, name="update_ads"),
    path('ads/<int:pk>/delete/', delete_ads, name="delete_ads"),
    path('ads/comment/add/<int:ads_id>/', save_comment, name="add_comment")
]