from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=10, null=False, unique=True)
    email = models.EmailField(max_length=200, null=False, unique=True)
    city = models.CharField(max_length=30, null=False)
    pincode = models.CharField(max_length=6, null=False)
    state = models.CharField(max_length=50, null=False)
    address_line_1 = models.CharField(max_length=300, null=False)
    address_line_2 = models.CharField(max_length=300, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
