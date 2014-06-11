from django.conf.urls import *

from views import *

urlpatterns = patterns('',
    url(r'^login/', login, name='cas_login'),
    url(r'^validate/', validate, name='cas_validate'),
    url(r'^logout/', logout, name='cas_logout'),
)
