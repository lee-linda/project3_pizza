from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User


from .models import Toppings, Pizza, RegularPizza, SicilianPizza, Subs, Sub_Additions, Pasta, Salads, DinnerPlatters, UserCart, UserOrder, OrderStatus, OrderNumber

# Create your views here.


def index(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    context = {
        "userlogged": request.user
    }
    return render(request, "orders/index.html", context)


def login_view(request):
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render(request, "orders/login.html", {"message": None})


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})


def register(request):
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        # Check if password and password confirmation are matching.
        if not password == password2:
            return render(request, "orders/register.html", {"message": "Passwords do not match."})
        # Check if username already exist in database.
        try:
            usernameExist = User.objects.get(username=username)
            return render(request, "orders/register.html", {"message": "Username is not available. Please try a different username."})
        except KeyError:
            return render(request, "orders/register.html", {"message": "Missing information in field."})
        except User.DoesNotExist:
            # If username is available, create entry into DB with user details
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            # Log new user in automatically after registering for new account
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render(request, "orders/register.html", {"message": None})


def menu(request, msg):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if msg == 'ItemAdded':
        message = "Item has been added. You can go to My Cart to proceed with order."
    elif msg == 'OrderPlaced':
        message = "Your order has been placed. You can go to My Order to check on your order status."
    else:
        message = None

    context = {
        "message": message,
        "userlogged": request.user
    }

    return render(request, "orders/menu.html", context)


def regularpizza(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    context = {
        "userlogged": request.user,
        "regularpizza": RegularPizza.objects.all().order_by('id'),
        "toppings": Toppings.objects.all().order_by('id'),
        "category": "Regular Pizza"
    }
    return render(request, "orders/regularpizza.html", context)


def sicilianpizza(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    context = {
        "userlogged": request.user,
        "sicilianpizza": SicilianPizza.objects.all().order_by('id'),
        "toppings": Toppings.objects.all().order_by('id'),
        "category": "Sicilian Pizza"
    }
    return render(request, "orders/sicilianpizza.html", context)


def subs(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    context = {
        "userlogged": request.user,
        "subs": Subs.objects.all().order_by('id'),
        "additions": Sub_Additions.objects.all().order_by('id'),
        "category": "Subs"
    }
    return render(request, "orders/subs.html", context)


def pasta(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    context = {
        "userlogged": request.user,
        "pasta": Pasta.objects.all().order_by('id'),
        "category": "Pasta"
    }
    return render(request, "orders/pasta.html", context)


def salads(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    context = {
        "userlogged": request.user,
        "salads": Salads.objects.all().order_by('id'),
        "category": "Salads"
    }
    return render(request, "orders/salads.html", context)


def dinnerplatters(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    context = {
        "userlogged": request.user,
        "dinnerplatters": DinnerPlatters.objects.all().order_by('id'),
        "category": "Dinner Platters"
    }
    return render(request, "orders/dinnerplatters.html", context)


def addtoCart(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if request.method == "POST":

        user_id = request.user.id
        category = request.POST["category"]
        item = request.POST["item"]
        addition = request.POST["addition"]
        size = request.POST["size"]
        quant = int(request.POST["quant"])
        priceEach = float(request.POST["priceEach"])

        cartItem = UserCart.objects.create(user_id=user_id, category=category, item=item, additions=addition,
                                           size=size, quantity=quant, priceEach=priceEach)
        cartItem.save()

        return HttpResponseRedirect(reverse("menu", args=("ItemAdded",)))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return HttpResponseRedirect(reverse("index"))


def myCart(request, msg):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    cartItems = UserCart.objects.filter(user_id=request.user.id).order_by('id')

    cartItemsLst = []
    total = 0

    for item in cartItems:
        myItem = {}
        myItem["itemID"] = item.id
        myItem["detailedItem"] = item.category + ' - ' + item.item
        if item.additions:
            myItem["addition"] = item.additions
        else:
            myItem["addition"] = ''
        myItem["size"] = item.size
        myItem["quantity"] = item.quantity
        myItem["priceEach"] = item.priceEach
        myItem["itemTotal"] = item.quantity * item.priceEach
        cartItemsLst.append(myItem)
        total += myItem["itemTotal"]

    if msg == 'Warning':
        message = "Quantity value is inappropriate."
    elif msg == 'NoItem':
        message = "No such item."
    elif msg == 'ItemUpdated':
        message = "Item has been updated."
    elif msg == 'ItemRemoved':
        message = "Item has been removed."
    elif msg == 'AllItemsRemoved':
        message = "All items are removed."
    else:
        message = None

    context = {
        "message": message,
        "userlogged": request.user,
        "cartItemsLst": cartItemsLst,
        "total": total
    }

    return render(request, "orders/myCart.html", context)


def update_quantity(request, itemID):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if request.method == "POST":

        updatedquantity = request.POST[str(itemID)]
        if updatedquantity == "":
            return HttpResponseRedirect(reverse("myCart", args=("Warning",)))
        else:
            try:
                ItemToUpdate = UserCart.objects.get(user_id=request.user.id, id=itemID)
                ItemToUpdate.quantity = int(updatedquantity)
                ItemToUpdate.save()
                return HttpResponseRedirect(reverse("myCart", args=("ItemUpdated",)))
            except UserCart.DoesNotExist:
                return HttpResponseRedirect(reverse("myCart", args=("NoItem",)))

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return HttpResponseRedirect(reverse("index"))


def deleteItem(request, itemID):
   # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if request.method == "POST":
        try:
            ItemToDelete = UserCart.objects.get(user_id=request.user.id, id=itemID)
            ItemToDelete.delete()
            return HttpResponseRedirect(reverse("myCart", args=("ItemRemoved",)))
        except UserCart.DoesNotExist:
            return HttpResponseRedirect(reverse("myCart", args=("NoItem",)))

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return HttpResponseRedirect(reverse("index"))


def deleteAllItem(request):
   # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if request.method == "POST":

        ItemsToDelete = UserCart.objects.filter(user_id=request.user.id)
        if ItemsToDelete.count() == 0:
            return HttpResponseRedirect(reverse("myCart", args=("NoItem",)))

        ItemsToDelete.delete()
        return HttpResponseRedirect(reverse("myCart", args=("AllItemsRemoved",)))

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return HttpResponseRedirect(reverse("index"))


def submitOrder(request):
   # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if request.method == "POST":
        # Get current order number, increase by 1 as current order confirmation number
        currentOrderNo = OrderNumber.objects.get(id=1)
        currentOrderNo.order_no = currentOrderNo.order_no + 1
        currentOrderNo.save()
        confirmationNo = currentOrderNo.order_no
        # Set status as pending for all items to be ordered
        statusPending = OrderStatus.objects.get(status="Pending")

        # Get items in user's cart
        cartItems = UserCart.objects.filter(user_id=request.user.id).order_by('id')

        for item in cartItems:
            orderItem = UserOrder.objects.create(order_no=confirmationNo, user_id=request.user.id, username=request.user.username,
                                                 category=item.category, item=item.item, additions=item.additions, size=item.size,
                                                 quantity=item.quantity, priceEach=item.priceEach, orderStatus=statusPending)
            orderItem.save()

        # Remove all items that have been ordered in user's cart
        ItemsToDelete = UserCart.objects.filter(user_id=request.user.id)
        ItemsToDelete.delete()

        return HttpResponseRedirect(reverse("menu", args=("OrderPlaced",)))

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return HttpResponseRedirect(reverse("index"))


def myOrder(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    orderItems = UserOrder.objects.filter(user_id=request.user.id).order_by('id')

    OrderNoLst = []
    uniqueNo = 0
    for item in orderItems:
        if item.order_no != uniqueNo:
            OrderNoLst.append(item.order_no)
            uniqueNo = item.order_no

    orderList = []
    for order in OrderNoLst:

        orderGroup = {}
        orderGroup["orderNo"] = order
        # Get items by this order number
        orderByNo = UserOrder.objects.filter(user_id=request.user.id, order_no=order).order_by('id')
        itemsByNo = []
        allStatusCompleted = 0
        total = 0

        for item in orderByNo:
            myItem = {}
            myItem["detailedItem"] = item.category + ' - ' + item.item
            if item.additions:
                myItem["addition"] = item.additions
            else:
                myItem["addition"] = ''
            myItem["size"] = item.size
            myItem["quantity"] = item.quantity
            myItem["priceEach"] = item.priceEach
            myItem["itemTotal"] = item.quantity * item.priceEach
            itemsByNo.append(myItem)
            total += myItem["itemTotal"]
            if item.orderStatus.status == 'Completed':
                allStatusCompleted += 1

        orderGroup["itemsByNo"] = itemsByNo
        orderGroup["total"] = total
        if allStatusCompleted == orderByNo.count():
            orderGroup["status"] = 'Completed'
        else:
            orderGroup["status"] = 'Pending'

        # Append order group by order number into main list
        # orderList [orderGroup{orderNo: , itemsByNo: itemsByNo[myItem{item key-pair values }, myItem{}, .. ] , total: ,  status:  }, orderGroup{}, orderGroup{}, orderGroup{}, ..]
        orderList.append(orderGroup)

    context = {
        "userlogged": request.user,
        "orderList": orderList
    }

    return render(request, "orders/myOrder.html", context)


def CustomerOrder(request):
    # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("index"))

    # Customer Order page only to be accessed and updated by superuser
    orderItems = UserOrder.objects.all().order_by('id')

    OrderNoLst = []
    uniqueNo = 0
    for item in orderItems:
        if item.order_no != uniqueNo:
            OrderNoLst.append(item.order_no)
            uniqueNo = item.order_no

    orderList = []
    for order in OrderNoLst:

        orderGroup = {}
        orderGroup["orderNo"] = order
        # Get items by this order number
        orderByNo = UserOrder.objects.filter(order_no=order).order_by('id')
        # Get customer ID to display name on page
        customerID = orderByNo[0].user_id
        customer = User.objects.get(id=customerID)
        orderGroup["customerName"] = customer.last_name + ', ' + customer.first_name

        itemsByNo = []
        allStatusCompleted = 0
        total = 0

        for item in orderByNo:
            myItem = {}
            myItem["detailedItem"] = item.category + ' - ' + item.item
            if item.additions:
                myItem["addition"] = item.additions
            else:
                myItem["addition"] = ''
            myItem["size"] = item.size
            myItem["quantity"] = item.quantity
            myItem["priceEach"] = item.priceEach
            myItem["itemTotal"] = item.quantity * item.priceEach
            itemsByNo.append(myItem)
            total += myItem["itemTotal"]
            if item.orderStatus.status == 'Completed':
                allStatusCompleted += 1

        orderGroup["itemsByNo"] = itemsByNo
        orderGroup["total"] = total
        if allStatusCompleted == orderByNo.count():
            orderGroup["status"] = OrderStatus.objects.get(status="Completed").id
        else:
            orderGroup["status"] = OrderStatus.objects.get(status="Pending").id

        # Append order group by order number into main list
        # orderList [orderGroup{orderNo: , itemsByNo: itemsByNo[myItem{item key-pair values }, myItem{}, .. ] , total: ,  status:  }, orderGroup{}, orderGroup{}, orderGroup{}, ..]
        orderList.append(orderGroup)

    context = {
        "userlogged": request.user,
        "orderList": orderList,
        "orderStatus": OrderStatus.objects.all().order_by('id')
    }

    return render(request, "orders/CustomerOrder.html", context)


def updateOrdStatus(request, orderNo):
   # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if request.method == "POST":
        updatedStatus = int(request.POST["status"])

        # Get user items with orderNo
        itemsToUpdate = UserOrder.objects.filter(order_no=orderNo)
        for item in itemsToUpdate:
            item.orderStatus_id = updatedStatus
            item.save()

        return HttpResponseRedirect(reverse("CustomerOrder"))

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return HttpResponseRedirect(reverse("index"))


def deleteOrder(request, orderNo):
   # Ensure that user is logged in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    if request.method == "POST":
        # Delete items with orderNo
        UserOrder.objects.filter(order_no=orderNo).delete()

        return HttpResponseRedirect(reverse("CustomerOrder"))

   # User reached route via GET (as by clicking a link or via redirect)
    else:
        return HttpResponseRedirect(reverse("index"))
