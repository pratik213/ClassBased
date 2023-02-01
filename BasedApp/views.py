from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from .models import DataModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import DataForm

class MyView(View):
    def get(self,request):
        return HttpResponse("Resultt")

class CreateData(CreateView):
    model=DataModel
    fields=['title','description']
    success_url="/"
    

class DataList(ListView):
    model=DataModel

class UpdateData(UpdateView):
    model=DataModel
    fields=[
        "title",
        "description",
    ]
    success_url="/"

class DeleteData(DeleteView):
    model=DataModel
    success_url="/"

class DataFormView(FormView):
    form_class=DataForm
    template_name="BasedApp/datamodel_form.html"
    success_url="/thanks/"

class DataDetailView(DetailView):
    model=DataModel
