from django.urls import path

from uploadapp.views import UploadCreateView, UploadUpdateView, GeneratePDF

app_name = 'uploadapp'

urlpatterns = [
    path('create/', UploadCreateView.as_view(), name='create'),
    path('update/<int:pk>', UploadUpdateView.as_view(), name='update'),
    path('pdf/<int:pk>', GeneratePDF.as_view(), name='pdf'),
]