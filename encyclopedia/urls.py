from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("test", views.test, name="test"),
    path("searched/<str:name>", views.searched, name="searched"),
    path("newpage", views.NewPage, name="newpage"),
    path("savepage", views.savepage, name="savepage"),
    path("editpage", views.editpage, name="editpage"),
    path("editted", views.editted, name="editted"),
    path("random", views.randompage, name="random")
]
