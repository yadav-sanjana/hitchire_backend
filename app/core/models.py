from django.db import models
from django.contrib.auth.models import User

class RecruiterModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


class CandidateModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.ManyToManyField('Skill', related_name='candidates')

    def __str__(self):
        return self.user.username


class AddressModel(models.Model):
    candidate = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.state}"


class EducationModel(models.Model):
    candidate = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    graduation_date = models.DateField()

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.school_name}"


class SkillModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ApplicationModel(models.Model):
    candidate = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(RecruiterModel, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.user.username} - {self.job_title}"
