from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=300)
    address_line_1 = models.CharField(max_length=300, null=False)
    address_line_2 = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name