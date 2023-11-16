# job_board/models.py
from django.db import models

class JobPosting(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50)
    industry = models.CharField(max_length=255)
    job_description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    education_requirements = models.CharField(max_length=255)
    experience_level = models.CharField(max_length=50)
    salary_or_compensation = models.CharField(max_length=255)
    application_deadline = models.DateField()
    application_instructions = models.TextField()
    application_url_or_email = models.CharField(max_length=255)
    benefits = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    company_description = models.TextField()
    contact_information = models.TextField()
    tags_or_keywords = models.CharField(max_length=255)
    job_id = models.CharField(max_length=50, unique=True)
    job_posting_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    