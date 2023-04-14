from django.urls import path
from . import views

urlpatterns = [
    path('',views.todolist,name='index'),
    path('update/<str:pk>',views.updateitem,name='update'),
    path('delete/<str:pk>',views.deleteitem,name='delete'),
    path('register/',views.register,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
]