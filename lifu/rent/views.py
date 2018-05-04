# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import User, Cloth, Order

# 用户主页面

def index(request):
    men_cloth_objs = Cloth.objects.filter(type="男").filter(count__gt=0)
    women_cloth_objs = Cloth.objects.filter(type="女").filter(count__gt=0)
    username = False
    return render_to_response("index.html", {"request": request, "username": username, "men_cloth_objs": men_cloth_objs,
                                             "women_cloth_objs": women_cloth_objs})

def user_index(request, username):
    global login_user_name
    login_user_name = username
    men_cloth_objs = Cloth.objects.filter(type="男").filter(count__gt=0)
    women_cloth_objs = Cloth.objects.filter(type="女").filter(count__gt=0)
    return render_to_response("index.html", {"username": username, "men_cloth_objs": men_cloth_objs, "women_cloth_objs": women_cloth_objs})

def user_login_view(request):
    return render_to_response("user_login.html")

def user_login(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    customer_obj = User.objects.get(email=email)
    if str(password) == customer_obj.password and str(customer_obj.sign) == "0":
        return HttpResponseRedirect("/user_index/%s" % (customer_obj.username))
    elif str(password) == customer_obj.password and str(customer_obj.sign) == "1":
        return HttpResponseRedirect("/admin_index/%s" % (customer_obj.username))
    else:
        return HttpResponseRedirect("/")

def user_register_view(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    password = request.GET.get("password")
    User.objects.create(username=name, email=email, password=password)
    return render_to_response("user_register.html")

def user_register(request):
    username = request.GET.get("name")
    email = request.GET.get("email")
    password = request.GET.get("password")
    User.objects.create(username=username, email=email, password=password, sign=0)
    return HttpResponseRedirect("/user_login_view")

def user_info_view(request):
    user_obj = User.objects.get(username=login_user_name)
    order_objs = Order.objects.filter(email=user_obj.email)
    username = user_obj.username
    name = user_obj.name
    email = user_obj.email
    sex = user_obj.sex
    address = user_obj.address
    phone = user_obj.phone
    return render_to_response("user_info.html", {"request": request, "order_objs": order_objs, "username": username,
                                                 "name": name, "email": email, "sex": sex,
                                                 "address": address, "phone": phone})

def user_update_info(request):
    username = request.GET.get("username")
    sex = request.GET.get("sex")
    name = request.GET.get("name")
    address = request.GET.get("address")
    phone = request.GET.get("phone")
    User.objects.filter(username=login_user_name).update(username=username, sex=sex, name=name,
                                                         address=address, phone=phone)
    return HttpResponseRedirect("/user_info_view")

def user_update_order(request):
    pass

def user_cancel_order(request):
    # 逻辑 删除订单表用户对应的数据，并且cloth表对应的服装加1
    user_obj = User.objects.get(username=login_user_name)
    Order.objects.filter(email=user_obj.email).delete()
    return HttpResponseRedirect("/user_info_view")

def user_change_password(request):
    user_obj = User.objects.get(username=login_user_name)
    old_password = request.GET.get("old_password")
    new_password = request.GET.get("new_password")
    confirm_password = request.GET.get("confirm_password")
    if str(user_obj.password) == str(old_password) and str(new_password) == str(confirm_password):
        User.objects.filter(username=user_obj.username).update(password=new_password)
    return HttpResponseRedirect("/user_info_view")

# 用户下单页面
def user_order_view(request):
    cloth_id = request.GET.get("id")
    cloth_obj = Cloth.objects.get(id=cloth_id)
    return render_to_response("user_order.html", {"request": request, "username": login_user_name, "cloth_obj": cloth_obj})

# 用户下单逻辑
def user_order(request):
    import time
    cloth_id = request.GET.get("id")
    user_obj = User.objects.get(username=login_user_name)
    cloth_obj = Cloth.objects.get(id=cloth_id)
    # 订购成功后 需要在cloth表中count减一 并且对于Order表默认的count为1 现在不考虑一个订单多个服装 DATE:5-3 23:06
    cloth_count = cloth_obj.count - 1
    Cloth.objects.filter(id=cloth_obj.id).update(count=cloth_count)
    phone = request.GET.get("phone")
    address = request.GET.get("address")
    order_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取现在时间为订单时间
    rent_time = request.GET.get("datetime") # 获取租赁时间
    orderState = "已预约" # 订单默认状态为"已预约"
    Order.objects.create(phone=phone, email=user_obj.email ,cus_name=user_obj.name, address=address, count=1, money=cloth_obj.cloth_price, clothName=cloth_obj.clothName, orderState=orderState, order_time=order_time, rent_time=rent_time)
    return HttpResponseRedirect("/user_info_view")

# 用户租赁流程
def user_rent_flow(request):
    return render_to_response("user_rent_flow.html", {"request": request, "username": login_user_name})

def user_address(request):
    return render_to_response("user_address.html", {"request": request, "username": login_user_name})