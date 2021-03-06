"""DjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.views.static import serve as dj_v_serve
from . import views
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('user_authentication.urls')),
    url(r'^notes/', include('notes.urls')),
    url(r'^$', views.main_page, name='main_page'),
    url(r'^grades/', include('grades.urls')),
    url(r'^kalendar/', include('kalendar.urls')),
    url(r'^poll/', include('poll.urls', namespace='poll')),
    url(r'^media/(.*)$', dj_v_serve, {'document_root' : settings.MEDIA_ROOT}),
    url(r'^ocr/', include('ocr.urls', namespace='ocr')),
    url(r'^notice_board/', include('notice_board.urls', namespace='notice_board', app_name='notice_board')),
]

