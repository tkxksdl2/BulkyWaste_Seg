# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

from uploadapp.forms import UploadCreationForm
from uploadapp.models import Upload

import googlemaps

from uploadapp.utils import render_to_pdf

import tensorflow as tf
import numpy as np
from numpy import argmax
from tensorflow.keras.models import load_model
from PIL import Image
import warnings


gmaps = googlemaps.Client(key='AIzaSyCCpe1QXfMoezcFO-eCX4Su_XDRwFuu3nQ')


class UploadCreateView(CreateView):
    model = Upload
    form_class = UploadCreationForm
    template_name = 'uploadapp/create.html'

    def form_valid(self, form):
        temp_upload = form.save(commit=False)
        temp_upload.save()

        temp_upload = form.save(commit=False)
        path = 'C:\\Users\\oooh3\\PycharmProjects\\djangoProject1\\media\\' + str(temp_upload.image)
        img = Image.open(path)
        result = trash_pred(img)

        temp_upload.price = separ_price(result)
        temp_upload.label = result


        g = gmaps.reverse_geocode((form.data.get('location')), language='ko')
        form.instance.location = g[0]['formatted_address']

        temp_upload.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('uploadapp:update', kwargs={'pk': self.object.pk})



class UploadUpdateView(UpdateView):
    model = Upload
    form_class = UploadCreationForm
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

class GeneratePDF(View):

    model = Upload
    context_object_name = 'target_upload'
    success_url = reverse_lazy('uploadapp:create')

    def get(self, request, *args, **kwargs):
        template = get_template('uploadapp/detail.html')
        qs = Upload.objects.get(pk=kwargs['pk'])
        context = {'qs': qs}

        pdf = render_to_pdf('uploadapp/detail.html', context)
        if pdf:
            return HttpResponse(pdf, content_type='application/pdf')  # TILL HERE HTML TO PDF
        return HttpResponse("Not found")

def trash_pred(img):
    warnings.filterwarnings(action='ignore')
    new_model = tf.keras.models.load_model('C:\\Users\\oooh3\\PycharmProjects\\djangoProject1\\my_model')
    label_filter = ['침대', '밥상', '서랍장', '수납장', '의자', '선풍기', '냉장고', '장농', '책상', '소파']

    images = []

    img_resized = img.resize([224, 224])
    pixels = np.array(img_resized)
    images.append(pixels)
    X = np.asarray(images, dtype=np.float32)
    xhat = X / 255.0
    yhat = new_model.predict(xhat)
    return label_filter[np.argmax(yhat)]

def separ_price(result):
    label_filter = ['침대', '밥상', '서랍장', '수납장', '의자', '선풍기', '냉장고', '장농', '책상', '소파']
    if result == label_filter[0]:
        return 11000
    if result == label_filter[1]:
        return 4000
    if result == label_filter[2]:
        return 7000
    if result == label_filter[3]:
        return 8000
    if result == label_filter[4]:
        return 3000
    if result == label_filter[5]:
        return 3000
    if result == label_filter[6]:
        return 10000
    if result == label_filter[7]:
        return 10000
    if result == label_filter[8]:
        return 7000
    if result == label_filter[9]:
        return 13000