from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page_title>", views.wiki_entry, name="wiki_entry")
]
