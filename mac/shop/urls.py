
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home),
    path('contact',views.contact),
    path('tracker',views.tracker),
    path('product',views.prodview),
    path('about',views.about),
    ]
