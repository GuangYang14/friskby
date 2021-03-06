from   django.conf.urls import url, include
from   django.core.urlresolvers import reverse

from views import Root
from views import PlotView,PlotGet

urlpatterns = [
    url(r'^$' , Root.as_view() , name = "plot_root"),
    url(r'^get/([0-9]+)/$'  , PlotGet.as_view() , name = "plot_get"),
    url(r'^view/([0-9]+)/$' , PlotView.as_view() , name = "plot_one")
]
