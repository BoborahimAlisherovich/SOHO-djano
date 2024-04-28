from django.urls import path
from .views import home_view, about_view,about2_view,gallery_view,contact_view,homepage2_view,homepage3_view

urlpatterns = [
    path('', home_view, name="home-page"),
    path('about/', about_view, name="about-page"),
    path('about-2/', about2_view, name="about-2-page"),
    path('contact/', contact_view, name="contact-page"),
    path('homepage-2/', homepage2_view, name="homepage-2-page"),
    path('gallery/', gallery_view, name="gallery-page"),
    path('homepage-3/', homepage3_view, name="homepage-3-page"),
]
