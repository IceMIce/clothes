from django.conf.urls import url
from django.contrib import admin
from rent import views as rent_views  # new
from rent import admin_views as admin_views


urlpatterns = [
    # User
    url(r'^$', rent_views.index),
    url(r'^user_login_view', rent_views.user_login_view),
    url(r'^user_login', rent_views.user_login),
    url(r'^user_register_view', rent_views.user_register_view),
    url(r'^user_register', rent_views.user_register),
    url(r'^user_index/([^\s/]+)/', rent_views.user_index),
    url(r'^user_info_view', rent_views.user_info_view),
    url(r'^user_update_info', rent_views.user_update_info),
    url(r'^user_change_password', rent_views.user_change_password),
    url(r'^user_rent_flow', rent_views.user_rent_flow),
    url(r'^user_order_view', rent_views.user_order_view),
    url(r'^user_order', rent_views.user_order),
    url(r'^user_cancel_order', rent_views.user_cancel_order),
    url(r'^user_update_order', rent_views.user_update_order),
    url(r'^user_address', rent_views.user_address),


    # admin
    url(r'^admin_index/([^\s/]+)/', admin_views.admin_index_view),
    url(r'^admin_user_info_view', admin_views.admin_user_info_view),
    url(r'^admin_update_user_info', admin_views.admin_update_user_info),
    url(r'^admin_change_password_view', admin_views.admin_change_password_view),
    url(r'^admin_change_password', admin_views.admin_change_password),
    url(r'^admin_order_view', admin_views.admin_order_view),
    url(r'^admin_delete_order', admin_views.admin_delete_order),
    url(r'^admin_update_order', admin_views.admin_update_order),
    url(r'^admin_user_view', admin_views.admin_user_view),
    url(r'^admin_update_user', admin_views.admin_update_user),
    url(r'^admin_delete_user', admin_views.admin_delete_user),
    url(r'^admin_admin_view', admin_views.admin_admin_view),
    url(r'^admin_update_admin', admin_views.admin_update_admin),
    url(r'^admin_delete_admin', admin_views.admin_delete_admin),
    url(r'^admin_clothes_view', admin_views.admin_clothes_view),
    url(r'^admin_add_clothes_view', admin_views.admin_add_clothes_view),
    url(r'^admin_add_clothes', admin_views.admin_add_clothes),
    url(r'^admin_delete_clothes', admin_views.admin_delete_clothes),
    url(r'^admin_update_clothes', admin_views.admin_update_clothes),
    url(r'^admin_feedback_view', admin_views.admin_feedback_view),
]