from django.db import models

class Risk(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    severity = models.CharField(max_length=50)
    likelihood = models.CharField(max_length=50)
    mitigation_plan = models.TextField(blank=True)

    def __str__(self):
        return self.name


