from django.shortcuts import render
from django.views.generic.base import View
from blog.core.models import Tutorial


class Home(View):
    def get(self, request):
        tutorial = Tutorial.objects.last()
        context = {
            'conteudo': tutorial,
        }
        return render(request, 'core/index.html', context)