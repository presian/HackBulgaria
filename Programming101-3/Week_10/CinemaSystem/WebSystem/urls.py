from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('WebSystem.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^reservations/([0-9]{1,4})/$', 'showReservationForm', name='regForm'),
                       ) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
