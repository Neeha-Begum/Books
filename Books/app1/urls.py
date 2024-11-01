from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.homeview,name="homepage"),
    path('book',views.bookview,name="book"),
    path('author',views.authorview,name="authorpage"),
    path('delete/<int:rid>',views.deleteview,name="deletepost"),
    #path('update/<int:pid>',views.updateview,name="updatepage"),
]