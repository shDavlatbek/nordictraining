from django.urls import path, include, re_path
from .views import HomeView, ContactView, \
NewsView, AboutView, AboutUniversityView, StaffView, \
PartnersView, RegisterView, TeacherTrainingView, ProgramDetailsView, \
NewsDetailView, NotFoundView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('contact/', ContactView.as_view(), name='contact'),
  path('about/', AboutView.as_view(), name='about'),
  path('about-university/', AboutUniversityView.as_view(), name='about-university'),
  path('staff/', StaffView.as_view(), name='staff'),
  path('partners/', PartnersView.as_view(), name='partners'),
  path('register/', RegisterView.as_view(), name='register'),
  path('teacher-training/', TeacherTrainingView.as_view(), name='teacher-training'),
  path('program-details/', ProgramDetailsView.as_view(), name='program-details'),
  path('news/', NewsView.as_view(), name='news'),
  path('news/<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),
  # path('hotel/<', HotelView.as_view(), name='hotel'),
  re_path(r'^.*$', NotFoundView.as_view(), name='not-found'),
]

