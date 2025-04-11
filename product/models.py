from django.db import models

class Noutbooks(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Noutbook"
        verbose_name_plural = "Noutbooks"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.brand} {self.model}"
