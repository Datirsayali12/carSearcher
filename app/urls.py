from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views




urlpatterns = [
    path('home/',views.home_page,name="home"),
    path('login-home/',views.login_home,name="login_home"),
    path('list/', views.list_view, name="list"),
    path('single-item/<str:id>/',views.show_single_item,name="single_item"),
    path('edit/<str:id>',views.edit_listing_page,name="edit"),
    path('like/<str:id>',views.like_listing_view,name="like"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)