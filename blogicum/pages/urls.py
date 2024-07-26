from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'pages'

# urlpatterns = [
#     path('about/', views.about, name='about'),
#     path('rules/', views.rules, name='rules'),
# ]


urlpatterns = [
    path(
        'about/', TemplateView.as_view(template_name='pages/about.html'),
        name='about'
    ),
    path(
        'rules/', TemplateView.as_view(template_name='pages/rules.html'),
        name='rules'
    ),
]
