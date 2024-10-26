# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite

from authentication.models import User, Challenge, Team, Participant

class CustomAdminSite(AdminSite):
    site_header = "Моя Админ Панель"  # Заголовок
    site_title = "Админка"  # Заголовок страницы
    index_title = "Добро пожаловать в мою админ панель"  # Заголовок на главной странице админки

# Создаем экземпляр вашего кастомного админ сайта
custom_admin_site = CustomAdminSite(name='custom_admin')

admin.site.register(User)
admin.site.register(Challenge)
admin.site.register(Team)
admin.site.register(Participant)
#
#
# admin.site.unregister(User)
# admin.site.unregister(Challenge)
# admin.site.unregister(Team)
# admin.site.unregister(Participant)

# custom_admin_site.register(User)
# custom_admin_site.register(Challenge)
# custom_admin_site.register(Team)
# custom_admin_site.register(Participant)

