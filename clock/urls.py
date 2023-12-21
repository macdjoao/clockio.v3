from django.urls import path

from clock.views import Clock


urlpatterns = [
    path('', Clock.as_view(), name='clock'),
]
