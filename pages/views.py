from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render, redirect




#Create your views here.
#def homePageView(request):
    #return HttpResponse('<h1> hello world</h1>')



class homePageView(TemplateView):
    template_name = 'pages/home.html'

class SuccesView(TemplateView):
    template_name = 'pages/formsucces.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "subtitle": "Product create",
            "description": "the form was sent successfully",
        })

        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Jaime Uribe",
        })

        return context
    
class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV","price":850},
        {"id":"2", "name":"iPhone", "description":"Best iPhone","price":699},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast","price":25},
        {"id":"4", "name":"Glasses", "description":"Best Glasses","price":14.99}
    ]

class ProductIndexView(View):
    template_name = 'pages/products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'pages/products/show.html'


    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id)-1]
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] =  product["name"] + " - Product information"
            viewData["product"] = product

            return render(request, self.template_name, viewData)
        except IndexError:
             return HttpResponseRedirect(reverse('home'))
    

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact us - Online Store",
            "subtitle": "Contact us",
            "email": "jruribem@eafit.edu.co",
            "address": "col",
            "phone": "000000000",
        })

        return context

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero")
        return price


class ProductCreateView(View):
    template_name = 'pages/products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('succes') 
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

