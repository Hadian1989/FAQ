from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.


def show_categories(request):
    return render(request, "categories.html", {'categories': Category.objects.all()})


class HomePageView(TemplateView):
    template_name = 'home.html'
