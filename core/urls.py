from django.urls import include, path

from core.views import TargetIndex, TargetCreate, TargetList, TargetUpdate, TargetDelete

app_name = 'core'

urlpatterns = [
    path('index/', TargetIndex.as_view(), name='index'),
    path('list/', TargetList.as_view(), name='list'),
    path('create/', TargetCreate.as_view(), name='create'),
    path('update/<int:pk>/', TargetUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TargetDelete.as_view(), name='delete'),
]