from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^connectors/', include('connectors.urls')),
	url(r'^authorization_manager/', include('authorization_manager.urls')),
	#url(r'^application_manager/', include('application_manager.urls')), #used via django admin atm
	url(r'^platform_api/', include('platform_manager.urls')),
	url(r'^openid/', include('django_openid_auth.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^quit/', 'application_manager.quit.quit'),
	url(r'^logout/', 'application_manager.logout.logout', name='logout'),

	url(r'^changebrowser', 'render.views.changebrowser', name='changebrowser'),
	url(r'^noscript', 'render.views.noscript', name='noscript'),
	 
	url(r'^test/', include('testing.urls')),
   	url(r'^auditing/', include('auditing.urls')),
	url(r'^', include('render.urls')),
	
)
