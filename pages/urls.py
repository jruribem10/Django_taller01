from django.urls import path
from .views import homePageView,AboutPageView,ContactPageView,ProductIndexView,ProductShowView,ProductCreateView,SuccesView
	
urlpatterns = [
    path("", homePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('formsucces/', SuccesView.as_view(), name='succes'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),

]