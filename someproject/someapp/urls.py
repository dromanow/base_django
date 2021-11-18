from django.urls import path

from .views import SomeModelView


urlpatterns = [
    path('', SomeModelView.as_view())
]
