from django.shortcuts import render
from django.views.generic.list import ListView
from .models import SomeModel

# Create your views here.


class SomeModelView(ListView):
    model = SomeModel
    template_name = 'index.html'
    queryset = SomeModel.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'user': {'name': 'Denis', 'age': 41}
        })
        return context
