from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('meet-the-editor/', views.MeetTheEditorView.as_view(), name='meet_the_editor'),
]