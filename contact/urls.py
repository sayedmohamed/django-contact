from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'contact.views',
    
    url(r'thanks/', 'thanks', name="contact_thanks"),
    url(r'ajax/', 'ajax', name="contact_ajax"),
    url(r'', 'index', name="contact_index"),
)
