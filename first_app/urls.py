from django.urls import path, re_path
from first_app.views import *

urlpatterns = [
    path('first_app/', first_app),
    # re_path(r'^book/(?<page_num>[0-9]{2})/$'),
    path('about/', about),
    path('img/', img1),
    path('json/', json),
    path('portfolio/', portfolio, name='portfolio page'),
    path('', about, name='about page'),
    path('', main, name='about page'),
]