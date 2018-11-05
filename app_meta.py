from django.conf.urls import url
from objectpack import desktop
from app.controller import controller
from m3.actions import ActionController, urls
from .actions import ContentTypePack, UserPack, GroupPack, PermissionPack
from django.contrib.contenttypes.models import ContentType


def register_urlpatterns():
   """
   Регистрация конфигурации урлов для приложения
   """
   return [url(*controller.urlpattern)]


def register_desktop_menu():
   """
   регистрация элеметов рабочего стола
   """

   desktop.uificate_the_controller(
       controller,
       menu_root=desktop.MainMenu.SubMenu('Демо')
   )

def register_actions():
    controller.packs.extend([
      ContentTypePack(),
      UserPack(),
      GroupPack(),
      PermissionPack(),
    ])  
