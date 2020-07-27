from django.db import models

class Pizza(models.Model):
    """A name field for pizza."""
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the model."""
        return self.name

class Topping(models.Model):
    """A Topping field for pizza toppings."""
    pizza = models.ForeignKey(
        'Pizza',
        on_delete = models.CASCADE
    )
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the model."""
        return self.name

class Entry(models.Model):
    """Something specific about each topping."""
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
        def __str__(self):
            """Return a string representation of the model."""
            return f"{self.text[:50]}..."
