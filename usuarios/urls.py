from django.conf.urls import url

from . import views
from .views import IndexUsuario, RegistroUsuario


urlpatterns = [
    url(r'^$', IndexUsuario.as_view(),  name='index'),
    url(r'^registro/$', RegistroUsuario.as_view(),  name='registrar'),




]



