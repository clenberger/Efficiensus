from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Shoe
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
class PageListView(ListView):
    model = Shoe
    
    def get(self, request):
        shoes = self.get_queryset().all()
        return render(request, 'shoes/list.html', {"shoes": shoes})
    
    
    
def hoodie_index(request):
    hoodies_list = Shoe.objects.all()
    context = {"shoes_list": hoodies_list,}
    template = loader.get_template('shoes/index.html')
    
    return HttpResponse(template.render(context, request))
