from django.urls import path
from site1 import views
from .views import HomePageView, GalleryPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
]