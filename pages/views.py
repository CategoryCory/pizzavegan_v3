from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from articles.models import ArticleSinglePage

from contacts.forms import ContactUsForm


def homepage_view(request):
    articles_list = ArticleSinglePage.objects.live().order_by('-first_published_at')[:6]

    context = {
        'articles_list': articles_list
    }

    return render(request, 'pages/home.html', context)


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class MeetTheEditorView(TemplateView):
    template_name = 'pages/meet-the-editor.html'


class ContactUsView(SuccessMessageMixin, CreateView):
    form_class = ContactUsForm
    template_name = 'pages/contact.html'
    success_url = reverse_lazy('pages:contact_us')
    success_message = 'Thank you for contacting us! We will read your message and respond soon!'
