from django.views.generic import TemplateView
from django.shortcuts import render
from articles.models import ArticleSinglePage


def homepage_view(request):
    articles_list = ArticleSinglePage.objects.all().order_by('-first_published_at')[:6]

    context = {
        'articles_list': articles_list
    }

    return render(request, 'pages/home.html', context)


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class MeetTheEditorView(TemplateView):
    template_name = 'pages/meet-the-editor.html'
