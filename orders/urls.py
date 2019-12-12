from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("menu/<msg>", views.menu, name="menu"),
    path("regularpizza", views.regularpizza, name="regularpizza"),
    path("sicilianpizza", views.sicilianpizza, name="sicilianpizza"),
    path("subs", views.subs, name="subs"),
    path("pasta", views.pasta, name="pasta"),
    path("salads", views.salads, name="salads"),
    path("dinnerplatters", views.dinnerplatters, name="dinnerplatters"),
    path("addtoCart", views.addtoCart, name="addtoCart"),
    path("myCart/<msg>", views.myCart, name="myCart"),
    path("update_quantity/<int:itemID>", views.update_quantity, name="update_quantity"),
    path("deleteItem/<int:itemID>", views.deleteItem, name="deleteItem"),
    path("deleteAllItem", views.deleteAllItem, name="deleteAllItem"),
    path("submitOrder", views.submitOrder, name="submitOrder"),
    path("myOrder", views.myOrder, name="myOrder"),
    path("CustomerOrder", views.CustomerOrder, name="CustomerOrder"),
    path("updateOrdStatus/<int:orderNo>", views.updateOrdStatus, name="updateOrdStatus"),
    path("deleteOrder/<int:orderNo>", views.deleteOrder, name="deleteOrder")

]
