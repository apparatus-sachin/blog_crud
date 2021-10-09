from django.urls import path
from . import views 

urlpatterns=[
path("",views.home,name='home'),
path("blog_add",views.blog_add,name="blog_add"),
path("blog_edit/<int:id>",views.blog_edit,name="blog_edit"),
path("blog_update/<int:id>",views.blog_update,name="blog_update"),
path("blog_trash/<int:id>",views.blog_trash,name="blog_delete"),

]
