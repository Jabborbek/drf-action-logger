from django.urls import path

from log_test_app.views import SampleLogAPIView

urlpatterns = [
    path("test-log/", SampleLogAPIView.as_view()),
]
