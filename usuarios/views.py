from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from django.views import generic
from .forms import RegistroForm


class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuarios/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('licencias:index')

class IndexUsuario(generic.TemplateView):
    template_name = 'usuarios/index.html'


