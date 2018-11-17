from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^applicant/$', views.ApplicantApi.as_view(), name='applicant'),
    url(r'^street/$', views.StreetApi.as_view(), name='street'),
    url(r'^expiry/$', views.ExpirationApi.as_view(), name='expiration'),
    url(r'^truck/$', views.TruckListApi.as_view(), name='truck-create'),
    url(r'^truck/(?P<pk>[0-9]+)/$', views.TruckRetrieveApi.as_view(), name='truck-detail'),
    url(r'^assign-job/$', views.AssignTruckApi.as_view(), name='assign-truck'),
]