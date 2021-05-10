from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    # path('meet-the-editor/', views.MeetTheEditorView.as_view(), name='meet_the_editor'),
    path('contact/', views.ContactUsView.as_view(), name='contact_us'),
    # path('pizzavegan-signup/', views.pizzavegan_signup_view, name='pizzavegan_signup'),
    # path('register/', views.RegisterPizzeriaView.as_view(), name='register_pizzeria'),
]