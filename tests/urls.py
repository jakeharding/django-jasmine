"""Setup url to run tests."""

from django.conf.urls import include, url

urlpatterns = [
    url(r'^/', include("django_jasmine.urls"))
]
