from django.conf.urls import patterns, include, url
from student_interface.views import first,search,result

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',first),
    url(r'^search/',search),
    url(r'^result/',result),
#    url(r'^search/result.firstname=([a-z]*)&lastname=([a-z]*)/',result),
)
