from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^', TemplateView.as_view(template_name='base.html')),
)