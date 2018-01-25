from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^total$', views.accueil, name='accueil'),
    url(r'^(?P<slug>.+)$', views.lire_article, name='blog_lire'),
    url(r'^$', views.prof_add, name='prof_add'),
    
]