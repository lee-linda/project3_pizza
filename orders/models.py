from django.db import models

# Create your models here.


class Toppings(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"


class Pizza(models.Model):
    item = models.CharField(max_length=64)
    num_toppings = models.IntegerField()

    def __str__(self):
        return f"{self.item} - Toppings ({self.num_toppings})"


class RegularPizza(models.Model):
    item = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="Regpizza")
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item} - Small $ {self.small}, Large $ {self.large}"


class SicilianPizza(models.Model):
    item = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="Sicipizza")
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item} - Small $ {self.small}, Large $ {self.large}"


class Subs(models.Model):
    item = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        if self.small:
            return f"{self.item} - Small $ {self.small}, Large $ {self.large}"
        else:
            return f"{self.item} - Large $ {self.large}"


class Sub_Additions(models.Model):
    addition = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.addition} - Small $ {self.small}, Large $ {self.large}"


class Pasta(models.Model):
    item = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item} - $ {self.price}"


class Salads(models.Model):
    item = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item} - $ {self.price}"


class DinnerPlatters(models.Model):
    item = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item} - Small $ {self.small}, Large $ {self.large}"


class UserCart(models.Model):
    user_id = models.IntegerField()
    category = models.CharField(max_length=64)
    item = models.CharField(max_length=100)
    additions = models.CharField(max_length=500, null=True, blank=True)
    size = models.CharField(max_length=64, null=True, blank=True)
    quantity = models.IntegerField()
    priceEach = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user_id} - {self.category} ({self.item} - {self.additions}), {self.size}, Quantity: {self.quantity}, $ {self.priceEach}"


class OrderStatus(models.Model):
    status = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.status}"


class UserOrder(models.Model):
    order_no = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    category = models.CharField(max_length=64)
    item = models.CharField(max_length=100)
    additions = models.CharField(max_length=500, null=True, blank=True)
    size = models.CharField(max_length=64, null=True, blank=True)
    quantity = models.IntegerField()
    priceEach = models.DecimalField(max_digits=5, decimal_places=2)
    orderStatus = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, related_name="OrderStatus")

    def __str__(self):
        return f"{self.order_no} : ({self.username}) - {self.category} ({self.item} - {self.additions}), {self.size}, Quantity: {self.quantity}, $ {self.priceEach} - Status: {self.orderStatus}"


class OrderNumber(models.Model):
    order_no = models.IntegerField()

    def __str__(self):
        return f"{self.order_no}"
