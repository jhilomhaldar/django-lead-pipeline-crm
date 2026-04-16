from django.db import models


class Lead(models.Model):
    STATUS_NEW = 'New'
    STATUS_CONTACTED = 'Contacted'
    STATUS_QUALIFIED = 'Qualified'
    STATUS_LOST = 'Lost'

    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_CONTACTED, 'Contacted'),
        (STATUS_QUALIFIED, 'Qualified'),
        (STATUS_LOST, 'Lost'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''}".strip()