from django.urls import URLPattern, path

from . import views

app_name= 'Dapp'
urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('index/', views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics'),
    # path('topics/<int:topic_id>/', views.topic, name = 'topic'),
]