from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import RegisterView,ProfileView


urlpatterns = [
    path('login-page/',views.login_page,name="login"),
    path('register-page/', RegisterView.as_view(), name="register"),
    path('logout/',views.logout_page,name="logout"),
    path('profile/', ProfileView.as_view(), name="profile"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)