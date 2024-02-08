from django.urls import include, path

from core.views import TargetIndex, TargetCreate

app_name = 'core'

urlpatterns = [
    path('index/', TargetIndex.as_view(), name='index'),
    path('create/', TargetCreate.as_view(), name='create'),
    # path('update/', TargetIndex.as_view(), name='update'),
    # path('delete/', TargetIndex.as_view(), name='delete ')
]