from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views as accounts_views
from boards import views as boards_views
from django.views.generic import TemplateView
from .routers import router
from employee import views as employee_views
# from blog_posts import views

urlpatterns = [
    url(r'^blog_posts/', include(('blog_posts.urls','blog_posts'), namespace='blog_posts')),
    url(r'^$', boards_views.home, name='home'),
    url(r'^coins/', include('coins.urls')),
    # url(r'^myrestaurants/$', include('myrestaurants.urls', namespace='myrestaurants')),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', boards_views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', boards_views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^article/', TemplateView.as_view(template_name='index.html')),
    path('emp', employee_views.emp),  
    path('show',employee_views.show),  
    path('edit/<int:id>', employee_views.edit),  
    path('update/<int:id>', employee_views.update),  
    path('delete/<int:id>', employee_views.destroy)
    # url(r'^emp', views.emp),
    # url('', TemplateView.as_view(template_name='index.html')),

]
