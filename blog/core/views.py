from django.shortcuts import render
from django.views.generic.base import View
from blog.core.models import Preview, Tutorial, LifeResume, LifeContent
from django.utils import timezone


class Home(View):
    def get(self, request):
        life = LifeResume.objects.filter(pushised_data__lte=timezone.now()).order_by('pushised_data')
        posts = Preview.objects.filter(pushised_data__lte=timezone.now()).order_by('pushised_data')
        context = {
            'posts': posts,
            'life': life,
        }
        return render(request, 'core/index.html', context)


class TutorialContent(View):
    def get(self, request, value):
        tuto = Tutorial.objects.get(id_publish=value)
        life = LifeResume.objects.filter(pushised_data__lte=timezone.now()).order_by('pushised_data')
        context = {
            'life': life,
            'tuto': tuto,
        }

        return render(request, 'core/conteudo.html', context)


class LifeContentView(View):
    def get(self, request, value):
        posts = Preview.objects.filter(pushised_data__lte=timezone.now()).order_by('pushised_data')
        tuto = LifeContent.objects.get(id_publish=value)
        context = {
            'posts': posts,
            'tuto': tuto,
        }
        return render(request, 'core/life.html', context)
