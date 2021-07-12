from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactUsView.as_view(), name='contact_us'),
    path('privacy/', views.PrivacyPolicyView.as_view(), name='privacy'),
    path('terms-of-service/', views.TermsOfServiceView.as_view(), name='terms_of_service'),
]