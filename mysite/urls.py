from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.site_main_new, name='site_main'),
    # ex: /0/
    url(r'^(?P<id_arc_tree>[0-9]+)/$', views.site_main_new, name='site_main'),
    # ex: /tree/
    url(r'^tree/$', views.site_tree_test, name='site_tree'),
    url(r'^yandex_ac493dcd5af1d1e6.html', views.yandex_63a3d0a896e29e17, name='yandex_63a3d0a896e29e17'),
    # ex: /site_head/
    url(r'^site_head/$', views.site_head, name='site_head'),
    # ex: /site_navigator/
    url(r'^site_navigator/$', views.site_navigator, name='site_navigator'),
    # ex: /site_article/
    url(r'^site_article/$', views.site_article, name='site_article'),
    # ex: /wrapper/
    url(r'^wrapper/$', views.wrapper, name='wrapper'),
    ]

