from django.urls import path
from . import views

urlpatterns=[
    path("", views.home),
    path("list/", views.blog_list),
    path("create/", views.create_blog),
    path("myblogs/", views.myblogs),
    path("read/<id>/", views.read_blog),
    path("update/<id>/", views.update_blog),
    path("del/<id>/", views.delete_blog_get),
    path("del_confirm/<id>/", views.delete_confirm),
    path("read_myblog/<id>/", views.read_myblog)
]