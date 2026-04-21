from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    name = models.CharField(max_length=40, null=False)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Vacancy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True, null=True, default=':)')
    salary = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99999)])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.salary}$"
    
class Applicant(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='hello...', blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, default=1)
    wanted_salary = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99999)])

    def __str__(self):
        return f"{self.author.name}'s application"