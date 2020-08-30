from django.conf.urls import url
from . import views
from .views import StudentCreateView, StudentEditView, ParticularCallOfRollCreateView, CallOfRollView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^student/edit/(?P<pk>\d+)$', StudentEditView.as_view(), name='update_student'),
    url(r'^student/callofroll/(?P<cursus_id>\d+)$', CallOfRollView.as_view(), name='call_of_roll'),
    url(r'^student/particular-callofroll/$', ParticularCallOfRollCreateView.as_view(), name='particular_call_of_roll'),
    url(r'^history/$', views.call_of_roll_history, name='call_of_roll_history'),
    url(r'^history/search$', views.call_of_roll_history_search, name='call_of_roll_history_search'),
]