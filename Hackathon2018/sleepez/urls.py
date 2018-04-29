"""WebApp URL Configuration

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

from sleepez import views
from django.conf.urls import url

appname = 'sleepez'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^about/$', views.about, name='about'),
    url(r'^google-maps/$', views.google_maps, name='google-maps'),
    url(r'^update/', views.update, name='update'),
    url(r'^directions/(?P<origin>[\w-]+)-(?P<destination>\w+)/$', views.directions, name='directions'),
    url(r'^form/', views.search_form , name='update'),
    url(r'^host_form/', views.HostCreateView.as_view(), name="host_form"),
]
