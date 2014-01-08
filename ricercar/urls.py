from django.conf.urls import patterns, include, url
from ricercar.website.views.main import home
from django.contrib import admin
from ricercar.website.views.auth import LoginFormView
from ricercar.website.views.auth import LogoutView
admin.autodiscover()

urlpatterns = patterns('',
    # url du site principal

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', LoginFormView.as_view(), name="login-view"),
    url(r'^logout/', LogoutView.as_view(), name="logout-view"),

    url(r'^$', home),
    url(r'^projets/', 'ricercar.website.views.main.projets', name='projets'),
)


    # url du site principal
urlpatterns += patterns('ricercar.gesualdo.views',

    url(r'^gesualdo/', 'main.home', name='gesualdo'),

)
