from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blocean.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lounge$','bloceanapp.views.lounge',name='lounge'),
    url(r'^manage$','bloceanapp.views.adminPanel',name='adminpanel'),
    url(r'^ele_mnt$',TemplateView.as_view(template_name='bloceanapp/elements.html')),
    url(r'^$',TemplateView.as_view(template_name='bloceanapp/basic.html')),
)
