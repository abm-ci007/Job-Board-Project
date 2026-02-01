from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Contract', 'Contract'),
    ('Temporary', 'Temporary'),
    ('Internship', 'Internship'),
    ('Other', 'Other'),
)

def validate_not_niegative(value):
    if value < 0:
        raise ValidationError(
            'Please enter a positive value', 
            params={'value': value},
        )
    
def validate_salary(value):
    if value < 1000:
        raise ValidationError(
            "Please enter a valid salary greater than 1000$",
            params={'value': value},
        )


class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField()
    salary = models.DecimalField(max_digits= 10, decimal_places=2, validators=[validate_salary])
    # location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1, validators=[validate_not_niegative])
    experience = models.IntegerField(default=1, validators=[validate_not_niegative])
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL, 
        null=True, blank=True, 
        related_name='jobs'
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


    
