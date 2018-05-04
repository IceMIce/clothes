# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import User, Feedback, Cloth, Order


def admin_index_view(request, username):
    global user_name
    user_name = username
    return render_to_response("admin_index.html", {"request": request, "username": username})

def admin_user_info_view(request):
    user_obj = User.objects.get(username=user_name)
    name = user_obj.name
    email = user_obj.email
    username = user_obj.username
    phone = user_obj.phone
    return render_to_response("admin_user_info.html",
                              {"request": request, "username": user_name, "name": name, "email": email,
                               "user_name": username, "phone": phone})

def admin_update_user_info(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    username = request.GET.get("username")
    phone = request.GET.get("phone")
    User.objects.filter(username=user_name).update(name=name, email=email, username=username, phone=phone)
    return render_to_response("admin_index.html", {"request": request, "username": user_name,})

def admin_change_password_view(request):
    return render_to_response("admin_change_password.html", {"request": request, "username": user_name,})

def admin_change_password(request):
    old_password = request.GET.get("old_password")
    new_password = request.GET.get("new_password")
    confirm_password = request.GET.get("confirm_password")
    user_obj = User.objects.get(username=user_name)
    if str(user_obj.password) == str(old_password) and str(new_password) == str(confirm_password):
        User.objects.filter(username=user_obj.username).update(password=new_password)
        return render_to_response("admin_index.html", {"request": request, "username": user_name})

# 用于用户管理页面
def admin_user_view(request):
    user_objs = User.objects.filter(sign="1")
    return render_to_response("admin_user.html", {"request": request, "username": user_name, "user_objs": user_objs})

def admin_update_user(request):
    username = request.GET.get("username")
    name = request.GET.get("name")
    phone = request.GET.get("phone")
    sex = request.GET.get("sex")
    address = request.GET.get("address")
    User.objects.filter(username=user_name).update(username=username, name=name, phone=phone, sex=sex, address=address)
    return HttpResponseRedirect("/admin_user_view")

def admin_delete_user(request):
    id = request.GET.get("id")
    User.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_user_view")

# 获取管理员数据
def admin_admin_view(request):
    user_objs = User.objects.filter(sign="1")
    return render_to_response("admin_admin.html", {"request": request, "username": user_name, "user_objs": user_objs})

def admin_update_admin(request):
    username = request.GET.get("username")
    name = request.GET.get("name")
    User.objects.filter(username=user_name).update(username=username, name=name)
    return HttpResponseRedirect("/admin_admin_view")

def admin_delete_admin(request):
    id = request.GET.get("id")
    User.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_admin_view")

# 用户订单
def admin_order_view(request):
    order_objs = Order.objects.all()
    return render_to_response("admin_order.html", {"request": request, "username": user_name, "order_objs": order_objs})


def admin_update_order(request):
    order_id = request.GET.get("id")
    order_state = request.GET.get("orderState")
    Order.objects.filter(id=order_id).update(orderState=order_state)
    return HttpResponseRedirect("/admin_order_view")

def admin_delete_order(request):
    id = request.GET.get("id")
    Order.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_order_view")


# 衣服相关函数
def admin_clothes_view(request):
    cloth_objs = Cloth.objects.all()
    return render_to_response("admin_clothes.html", {"request": request, "username": user_name, "cloth_objs": cloth_objs})

def admin_add_clothes_view(request):
    return render_to_response("admin_add_clothes.html", {"request": request, "username": user_name,})

def admin_add_clothes(request):
    clothes_name = request.POST.get("clothes_name")
    price = request.POST.get("price")
    count = request.POST.get("count")
    # size = request.GET.get("size")
    picture = request.FILES.get("picture")
    Cloth.objects.create(clothName=clothes_name, count=count, price=price, picture=picture)
    return HttpResponseRedirect("/admin_add_clothes_view")

def admin_delete_clothes(request):
    id = request.GET.get("id")
    Cloth.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_clothes_view")

def admin_update_clothes(request):
    clothes_id = request.POST.get("id")
    clothes_name = request.POST.get("clothes_name")
    price = request.POST.get("price")
    count = request.POST.get("count")
    picture = request.FILES.get("picture")
    Cloth.objects.filter(id=clothes_id).update(clothName=clothes_name, count=count, price=price, picture=picture)
    return HttpResponseRedirect("/admin_clothes_view")

# 额外功能
def admin_feedback_view(request):
    feedback_objs = Feedback.objects.all()
    return render_to_response("admin_feedback.html", {"request": request, "username": user_name, "feedback_objs": feedback_objs})