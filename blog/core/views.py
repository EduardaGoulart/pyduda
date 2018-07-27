from django.shortcuts import render
from django.views.generic.base import View
from blog.core.models import Tutorial
from django.utils import timezone


class Home(View):
    def get(self, request):
        posts = Tutorial.objects.filter(pushised_data__lte=timezone.now()).order_by('pushised_data')
        # tutorial = Tutorial.objects.last()
        # print(tutorial.choice_set.count())
        context = {
            # 'conteudo': tutorial,
            'posts': posts,
        }
        return render(request, 'core/index.html', context)


class TutorialContent(View):
    def get(self, request):
        return render(request, 'core/conteudo.html')