# alerts_models.py
# Django Service: Database Model for Alert Logging & Parent Portal

from django.db import models

class Parent(models.Model):
    """Stores parent and guardian contact information."""
    camis_student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} ({self.camis_student_id})"

class AlertLog(models.Model):
    """Tracks every alert sent by the FastAPI Gateway."""
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=50) # e.g., 'FEE_DUE'
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    message_details = models.TextField()

    def __str__(self):
        return f"Alert {self.alert_type} to {self.parent}"
