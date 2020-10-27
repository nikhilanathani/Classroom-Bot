from django.conf.urls import url
from api.views import Course, Student, Group, Assignment, Schedule


urlpatterns = [url('course', Course.as_view(), name='course_url'),
               url('student', Student.as_view(), name='student_url'),
               url('group', Group.as_view(), name='group_url'),
               url('schedule', Schedule.as_view(), name='schedule_url'),
               url('assignment', Assignment.as_view(), name='assignment_url')]
