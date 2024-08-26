from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Contract(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    contract_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    contract_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.contract_title} ({self.vendor.name})"

class PerformanceRating(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    rating_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.vendor.name} - {self.rating}/5"

class Procurement(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_procurement = models.DateField()

    def __str__(self):
        return f"{self.item_description} ({self.vendor.name})"
