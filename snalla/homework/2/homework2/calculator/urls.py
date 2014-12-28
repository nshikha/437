from django.conf.urls import include, url

urlpatterns = [ 
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'calculator.views.calculate'),
]