from django.conf.urls import url
from django.contrib import admin
from rent import views as rent_views  # new

urlpatterns = [
    url(r'^$', rent_views.index),  # new
    url(r'^admin/', admin.site.urls),
]