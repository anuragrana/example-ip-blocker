from django_bot_crawler_blocker import views
from django.conf.urls import url, include

app_name = "django_bot_crawler_blocker"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]