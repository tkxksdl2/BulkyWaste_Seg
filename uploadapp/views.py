
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from uploadapp.forms import UploadCreationForm, UploadupdateForm
from uploadapp.models import Upload

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyCCpe1QXfMoezcFO-eCX4Su_XDRwFuu3nQ')


class UploadCreateView(CreateView):
    model = Upload
    form_class = UploadCreationForm
    template_name = 'uploadapp/create.html'

    def form_valid(self, form):
        g = gmaps.reverse_geocode((form.data.get('location')), language='ko')
        form.instance.location = g[0]['formatted_address']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('uploadapp:update', kwargs={'pk': self.object.pk})


class UploadUpdateView(UpdateView):
    model = Upload
    form_class = UploadupdateForm
    context_object_name = 'target_upload'
    template_name = 'uploadapp/update.html'

    def get_success_url(self):
        return reverse('uploadapp:update', kwargs={'pk': self.object.pk})


class UploadDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        upload = Upload.objects.get(pk=kwargs['pk'])
        upload.submit = True
        upload.save()
        return super().get(request, *args, **kwargs)

    model = Upload
    context_object_name = 'target_upload'
    template_name = 'uploadapp/detail.html'

