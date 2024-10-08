from django.urls import path

from .import views

urlpatterns = [
    path('',views.Home.as_view() , name= 'home'),
    path('s',views.SessionView.as_view() , name= 's'),
    path('mail', views.mailSendView , name= 'mail'),
    path('gallery', views.GalleryCreateView.as_view() , name= 'gallery'),
    path('register', views.RegisterView.as_view() , name= 'register'),
    path('login', views.LoginView.as_view() , name= 'login'),
    path('add-todo',views.TodoCreateView.as_view(), name= 'add_to-do'),
    path('delete-todo/<int:pk>',views.TodoDeleteView.as_view(), name = 'delete'),
    path('edit-todo/<int:pk>',views.TodoUpdateView.as_view(),name = 'edit')
]