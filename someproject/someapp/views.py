from django.shortcuts import render
from django.views.generic.list import ListView
from .models import SomeModel, SomeOtherModel


class SomeModelView(ListView):
    model = SomeModel
    template_name = 'index.html'
    queryset = SomeModel.objects.select_related('other').prefetch_related('other1').all()
    # queryset = SomeModel.objects.value_filter().select_related('other').prefetch_related('other1').all()
    # extra_context = {
    #     'user': {'name': 'Denis', 'age': 41}
    # }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'user': {'name': 'Denis', 'age': 41},
            'site': self.request.site
        })
        return context
