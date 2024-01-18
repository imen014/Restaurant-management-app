"""
URL configuration for RestaurantMenuPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from authentication.views import create_user, login_user, home, delete_users, get_users, logout_user, update_user, show_my_account, detele_my_account
from RestaurantMenuPro import settings
from django.conf.urls.static import static

from MenuApp.views import create_menu, get_menus, update_menu, delete_menu, create_eater, get_eaters, update_eater, delete_eater, show_eater
from command_food_app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', create_user, name='create_user'),
    path('',login_user,name='login_user'),
    path('home/<int:id>/user', home, name='home'),
    path('delete_users/', delete_users, name='delete_users'),
    path('get_users/', get_users, name='get_users'),
    path('logout_user/', logout_user, name='logout_user'),
    path('update_user/<int:id>/update_user', update_user, name='update_user'),
    path('show_my_account/<int:id>/show_account', show_my_account, name='show_my_account'),
    path('detele_my_account/<int:id>/delete', detele_my_account, name="detele_my_account"),
    path('create_menu/', create_menu, name='create_menu'),
    path('get_menus/', get_menus, name='get_menus'),
    path('update_menu/<int:id>/update', update_menu, name='update_menu'),
    path('delete_menu/<int:id>/delete', delete_menu, name='delete_menu'),
    path('create_eater/', create_eater, name='create_eater'),
    path('get_eaters/', get_eaters, name='get_eaters'),
    path('update_eater/<int:id>/update', update_eater, name="update_eater"),
    path('delete_eater/<int:id>', delete_eater, name="delete_eater"),
    path('show_eater/<int:id>/showit',show_eater,name="show_eater"),
    path('create_command/', views.create_command, name="create_command"),
    path('get_commands/<str:place_of_delivery>/find', views.get_commands, name="get_commands"),
    path('modify_command/<int:id>/modify', views.modify_command, name='modify_command'),
    path('commands_phone/<str:command_client_phone_number>/find', views.get_commands_by_phone_number, name="commands_phone"),
    path('get_my_commands/', views.get_my_commands, name="get_my_commands"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    