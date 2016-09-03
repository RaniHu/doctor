"""jkjydr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from userLoginin import views as userLoginin_views
from workMzBingli import views as workMzBingli_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'userLoginin.views.login', name='login'),
    url(r'^register/', 'userLoginin.views.register', name='register'),
    url(r'^startregister/', 'userLoginin.views.startregister', name='startregister'),
    url(r'^startlogin/', 'userLoginin.views.startlogin', name='startlogin'),
    url(r'^workregisterIndex/$', 'userLoginin.views.workregisterIndex', name='workregisterIndex'),
    url(r'^bingli/', 'workMzBingli.views.turnPage', name='turnPage'),
    url(r'^fbingli/', 'workMzFeiBingli.views.fbingli', name='fbingli'),
    url(r'^completed/', 'workSmCompleted.views.completed', name='completed'),
    url(r'^unread/', 'workSmUnread.views.unread', name='unread'),
    url(r'^depUnion/', 'depUnion.views.depUnion', name='depUnion'),
    url(r'^comment/', 'depUnion.views.comment', name='comment'),
    url(r'^pubContent/', 'depUnion.views.pubContent', name='pubContent'),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r"^media/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),

]
