from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views
from django.views.generic import TemplateView
from .routers import router

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^coins/', include('coins.urls')),
    # url(r'^myrestaurants/$', include('myrestaurants.urls', namespace='myrestaurants')),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^article/', TemplateView.as_view(template_name='index.html')),
    url('', TemplateView.as_view(template_name='index.html')),

]