from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest

from .models import Category, Ads, Comment
from .form import CommentForm, AdsForm


def home(request: HttpRequest):
    ads = Ads.objects.all()
    categories = Category.objects.all()
    context = {
        'ads': ads,
        'categories': categories,
        'title': "Barcha maqolalar"
    }
    return render(request, "main/index.html", context)


def ads_by_category(request: HttpRequest, category_id: int):
    ads = Ads.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    context = {
        'ads': ads,
        'categories': categories,
        'title': Category.objects.get(pk=category_id).name
    }
    return render(request, "main/index.html", context)


def ads_detail(request: HttpRequest, pk: int):
    ads = get_object_or_404(Ads, pk=pk, published = True)
    categories = Category.objects.all()
    comments = Comment.objects.filter(ads=ads)

    ads.views += 1
    ads.save()

    context = {
        "ads": ads,
        "categories": categories,
        "title": ads.title,
        "form": CommentForm(),
        "comments": comments
    }
    return render(request, "main/ad-details.html", context)


def save_comment(request: HttpRequest, ads_id: int):
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=request.POST.get("text"),
                ads_id=ads_id,
                user=request.user
            )
    return redirect("ads_detail", pk=ads_id)


def save_ads(request: HttpRequest):
    if request.user.is_staff:
        if request.method == "POST":
            form = AdsForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                ads = form.save()
                return redirect("ads_detail", pk=ads.pk)
        else:
            form = AdsForm()
        context = {
            "form": form,
        }
        return render(request, "main/ad-post.html", context)


def update_ads(request, pk: int):
    ads=get_object_or_404(Ads, pk=pk)
    if request.method == "POST":
        form = AdsForm(data=request.POST, files=request.FILES, instance=ads)
        if form.is_valid():
            ads = form.save()
            return redirect("ads_detail", pk=ads.pk)
    else:
        form = AdsForm(instance=ads)
    context = {
        "form": form
    }
    return render(request, "main/ad-post.html", context)


def delete_ads(request, pk:int):
    ads = get_object_or_404(Ads, pk=pk)
    if request.method == "POST":
        ads.delete()
        return redirect("home")
    else:
        context = {
            "title": ads.title
        }
        return render(request, "main/confirm-delete.html", context)