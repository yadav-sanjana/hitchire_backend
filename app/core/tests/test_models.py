from unittest.mock import patch
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

User = get_user_model()


class TestRecruiterModel(TestCase):
    def test_recruiter_model(self):
        #tests for the Recruiter model here
        pass


class TestCandidateModel(TestCase):
    def test_candidate_model(self):
        #tests for the Candidate model here
        pass


class TestAddressModel(TestCase):
    def test_address_model(self):
        #tests for the Address model here
        pass


class TestEducationModel(TestCase):
    def test_education_model(self):
        #tests for the Education model here
        pass


class TestEmploymentModel(TestCase):
    def test_employment_model(self):
        #tests for the EmploymentModel here
        pass


class TestSkillModel(TestCase):
    def test_skill_model(self):
        #tests for the SkillModel here
        pass


class TestProfileModel(TestCase):
    def test_profile_model(self):
        #tests for the ProfileModel here
        pass


class TestApplicationModel(TestCase):
    def test_application_model(self):
        #tests for the Application model here
        pass
