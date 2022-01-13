from django.urls import path

from .views import AboutPageView

app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
]