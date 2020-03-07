from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Hoodie
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
class PageListView(ListView):
    model = Hoodie
    
    def get(self, request):
        hoodies = self.get_queryset().all()
        return render(request, 'hoodies/list.html', {"hoodies": hoodies})
    
    
    
def hoodie_index(request):
    hoodies_list = Hoodie.objects.all()
    context = {"hoodies_list": hoodies_list,}
    template = loader.get_template('recipes/index.html')
    
    return HttpResponse(template.render(context, request))
    