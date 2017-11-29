from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView 
from .views import CreateFieldView
from .views import FieldListView 

urlpatterns = {
    url(r'^risktypes/$', CreateView.as_view(), name="create"),
    url(r'^risktypes/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^risktypefields/$', CreateFieldView.as_view(), name="createfield"),
    url(r'^risktypefields/(?P<id>[0-9]+)/$', FieldListView.as_view(), name="fielddetails"),
}

urlpatterns = format_suffix_patterns(urlpatterns)