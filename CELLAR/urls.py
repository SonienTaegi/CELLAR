from django.conf.urls import include, url
from django.contrib import admin

import Browser.urls
import Browser.views.cellar
from CELLAR import settings


urlpatterns = [
    # CELLAR Administrator page
    url(r'^admin/', include(admin.site.urls)),
    
    # External libraries
    url(r'^libs/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.BASE_DIR + '/Browser/libs'}),

    url(r'^$', Browser.views.cellar.main, name="cellar"),
    url(r'^', include(Browser.urls.urlpatterns)),
]

print(urlpatterns)
