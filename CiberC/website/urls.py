from django.conf.urls import url
from . import views


urlpatterns = [

    # /CiberC/
    url(r'^$', views.auth_login, name = 'auth_login'),

    #CiberC/registration/
    url(r'^registration/$', views.registration, name = 'registration'),

    #/CiberC/register/
    url(r'^register/$', views.register, name = 'register'),

    # /CiberC/main/
    url(r'^main/$', views.main, name = 'main'),

    #/CiberC/login_validation/
    url(r'^login_validation/$', views.login_validation, name = 'login_validation'),

    #/CiberC/uploadFile/
    url(r'^uploadFile/$', views.upload, name = 'uploadFile'),

    #/CiberC/uploadingFile/
    url(r'^uploadingFile/$', views.upload_file, name = 'uploadingFile'),

    #/CiberC/logout/
    url(r'^logout/$', views.auth_logout, name = 'auth_logout'),

    #/CiberC/downloadFile/
    url(r'^downloadFile/$', views.download, name = 'download'),

    # /CiberC/downloadingFile/
    url(r'^downloadingFile/$', views.download_file, name='downloadingFile'),

    #/CiberC/view/
    url(r'^view/$', views.view, name='view'),

    #/CiberC/viewGraph/
    url(r'^viewGraph/$', views.view_graph, name='view_graph'),

    #/CiberC/modules/
    url(r'^modules/$', views.modules, name='modules'),

    #/CiberC/convertModules/
    url(r'^convertModules/$', views.convertModules, name='convertModules')

    ]

