from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    # blank means mot required, null means it can be blank in the database
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("products:products", kwargs={"URLid": self.id})  # f"/products/{self.id}"
