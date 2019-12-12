from django.contrib import admin

from .models import Toppings, Pizza, RegularPizza, SicilianPizza, Subs, Sub_Additions, Pasta, Salads, DinnerPlatters, UserCart, UserOrder, OrderStatus, OrderNumber

# Register your models here.
admin.site.register(Toppings)
admin.site.register(Pizza)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Subs)
admin.site.register(Sub_Additions)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(UserCart)
admin.site.register(UserOrder)
admin.site.register(OrderStatus)
admin.site.register(OrderNumber)
