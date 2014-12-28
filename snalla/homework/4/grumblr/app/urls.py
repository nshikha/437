from django.conf.urls import patterns,include, url
from django.conf import settings

urlpatterns = patterns('', 
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login/login.html'}),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'login/login.html'}),
    url(r'^logout', 'django.contrib.auth.views.logout_then_login'),
    url(r'^register', 'app.views.register'),
    url(r'^feed', 'app.views.feed'),
    url(r'^search', 'app.views.search'),
    url(r'^users', 'app.views.users'),
    url(r'^edit', 'app.views.editProfile'),
    url(r'^profile/posts/(?P<post_id>\d+)$', 'app.views.comment'),
    url(r'^feed/posts/(?P<post_id>\d+)$', 'app.views.comment'),
    url(r'^profile/(?P<user_id>\d+)$', 'app.views.profile'),
    url(r'^follow/(?P<user_id>\d+)$', 'app.views.follow'),
    url(r'^block/(?P<user_id>\d+)$', 'app.views.block'),
    url(r'^profile', 'app.views.userprofile'),
    url(r'^profile/dislike/(?P<post_id>\d+)$', 'app.views.dislike'),
    url(r'^feed/dislike/(?P<post_id>\d+)$', 'app.views.dislike'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)