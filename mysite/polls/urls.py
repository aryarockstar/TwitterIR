from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
from polls import views

urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    url(r'^$', views.index, name='index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
#from django.conf.urls import include, url
#from django.contrib import admin

#urlpatterns = [
 #   url(r'^polls/', include('polls.urls')),
  #  url(r'^admin/', admin.site.urls),
#]
