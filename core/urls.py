from django.urls import include, path

from core.views import TargetIndex

app_name = 'core'

urlpatterns = [
    path('index/', TargetIndex.as_view(), name='index')
]