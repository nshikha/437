from django.conf.urls import patterns,include, url

urlpatterns = patterns('', 
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout', 'django.contrib.auth.views.logout_then_login'),
    url(r'^register', 'app.views.register'),
    url(r'^profile', 'app.views.profile'),
    url(r'^feed', 'app.views.feed'),
    url(r'^edit', 'app.views.editProfile'),
)