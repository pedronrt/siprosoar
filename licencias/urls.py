from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexLicencias.as_view(),  name='index'),

]





