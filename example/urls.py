from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('^qunit/', include('django_qunit.urls'))
)
