# job_board/urls.py
from django.urls import path
from .views import (
    JobPostingCreateView,
    JobPostingReadView,
    JobPostingUpdateView,
    JobPostingDeleteView,
)

urlpatterns = [
    path('job-postings/', JobPostingReadView.as_view(), name='job-posting-list'),
    path('job-postings/create/', JobPostingCreateView.as_view(), name='job-posting-create'),
    path('job-postings/update/<int:pk>/', JobPostingUpdateView.as_view(), name='job-posting-update'),
    path('job-postings/delete/<int:pk>/', JobPostingDeleteView.as_view(), name='job-posting-delete'),
]
