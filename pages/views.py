from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from articles.models import ArticleSinglePage

from contacts.forms import ContactUsForm, SurveyResponseForm, PizzeriaSignupResponseForm


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


class RegisterPizzeriaView(SuccessMessageMixin, CreateView):
    form_class = PizzeriaSignupResponseForm
    template_name = 'pages/register-pizzeria.html'
    success_url = reverse_lazy('pages:register_pizzeria')
    success_message = 'Your submission has been received! You will receive an email confirmation with additional ' \
                      'information and steps.'


def pizzavegan_signup_view(request):
    if request.method == 'POST':
        form = SurveyResponseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for signing up! We will let you know when we officially launch!'
            )
            return redirect('pages:pizzavegan_signup')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was a problem signing up. Please try again later.'
            )
            return redirect('pages:pizzavegan_signup')
    else:
        form = SurveyResponseForm()

    context = {
        'form': form,
    }

    return render(request, 'pages/pizzavegan-signup.html', context)
