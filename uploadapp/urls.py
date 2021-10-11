from django.urls import path

from uploadapp.views import UploadCreateView, UploadDetailView, UploadUpdateView

app_name = 'uploadapp'

urlpatterns = [
    path('create/', UploadCreateView.as_view(), name='create'),
    path('update/<int:pk>', UploadUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', UploadDetailView.as_view(), name='detail'),
]