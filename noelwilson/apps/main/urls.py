from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('noelwilson.apps.main.views',
    url(r'^$','homepage', name="main_home"),
    url(r'^technical/(?P<projectName>\w+)/$', 'technical', name="main_technicalVar"),
    url(r'^technical/$', 'technical', name="main_technical"),
    url(r'^artwork/(?P<projectName>\w+)/$', 'artwork', name="main_artworkVar"),
    url(r'^artwork/$', 'artwork', name="main_artwork"),
    url(r'^training/$', 'training', name="main_training"),
    url(r'^download/(?P<filePath>.+)/$', 'download', name="main_download"),
)

"""
url(r'^$',TemplateView.as_view(template_name="home.html"), name='main_home'),
url(r'^art/$', 'art', name='main_art'),
url(r'^training/$', 'training', name='main_training'),
url(r'^blog/$', 'blog', name='main_blog'),
"""


