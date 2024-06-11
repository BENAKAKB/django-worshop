

from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    aadhaar_number = models.CharField(max_length=12, unique=True)
    customer_id = models.IntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            last_customer = Customer.objects.all().order_by('customer_id').last()
            if last_customer:
                self.customer_id = last_customer.customer_id + 1
            else:
                self.customer_id = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} (ID: {self.customer_id})'
