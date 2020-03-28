from django.urls import path
from .views import HomePageView, AboutPageView, ContactsPageView, GalleryPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
]