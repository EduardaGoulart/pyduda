from django.shortcuts import render
from django.views.generic.base import View
from blog.core.models import Preview, Tutorial, PreviewLife, TutorialLife
from django.utils import timezone


class Home(View):
    def get(self, request):
        life = PreviewLife.objects.filter(pushised_data__lte=timezone.now()).order_by('pushised_data')
        posts = Preview.objects.filter(pushised_data__lte=timezone.now()).order_by('pushised_data')
        context = {
            'posts': posts,
            'life': life,
        }
        return render(request, 'core/index.html', context)


class TutorialContent(View):
    def get(self, request, value):
        tuto = Tutorial.objects.get(id_publish=value)
        context = {
            'tuto': tuto,
        }
        return render(request, 'core/conteudo.html', context)


class TutorialContentLife(View):
    def get(self, request, value):
        tuto = TutorialLife.objects.get(id_publish=value)
        context = {
            'tuto': tuto,
        }
        return render(request, 'core/life.html', context)
