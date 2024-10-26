# -- coding: utf8 --

from django.db import models

# class User(models.Model):
#     ROLE_CHOICES = [
#         ('user', 'User'),
#         ('admin', 'Admin'),
#     ]
#     full_name = models.CharField(max_length=255)
#     photo = models.CharField(max_length=255, blank=True)
#     interests = models.TextField(blank=True)
#     stats = models.TextField(blank=True)
#     about = models.TextField(blank=True)
#     registration_date = models.DateTimeField(auto_now_add=True)
#     email = models.EmailField(unique=True)
#     role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')
#
#     def __str__(self):
#         return self.full_name


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    profile_photo = models.ImageField(upload_to='photo_profile/', blank=True, verbose_name='Фото профиля')
    interests = models.TextField(verbose_name='Интересы')
    stats = models.TextField(verbose_name='Статистика')
    bio = models.TextField(verbose_name='О себе')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    email = models.EmailField(unique=True, verbose_name='Почта')

    # role = models.CharField(max_length=5, choices=[('user', 'User'), ('admin', 'Admin')])
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Challenge(models.Model):
    TYPE_CHOICES = [
        ('личный', 'Personal'),
        ('групповой', 'Group'),
        ('семейный', 'Family'),
    ]
    name = models.CharField(max_length=255, verbose_name='Название')
    icon = models.ImageField(upload_to='photo_icon/', blank=True, verbose_name='Иконка')
    image = models.ImageField(upload_to='photo_challenge/', blank=True, verbose_name='Шапка челенджа')
    description = models.TextField(verbose_name='О челендже')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Тип челенджа')
    is_team = models.BooleanField(default=False, verbose_name='Командный')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="challenges", verbose_name='Создатель')

    class Meta:
        verbose_name = "Челлендж"
        verbose_name_plural = "Челленджи"

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название команды')
    description = models.TextField(blank=True, verbose_name='О команде')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teams", verbose_name='Капитан')

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self):
        return self.name


class Participant(models.Model):
    STATUS_CHOICES = [
        ('в_процессе', 'In Progress'),
        ('завершён', 'Completed'),
        ('отказ', 'Rejected'),
    ]
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name="participants", verbose_name='Челендж')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participations", verbose_name='Пользователь')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="participants", verbose_name='Команда')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус')
    progress = models.JSONField(default=dict, blank=True, verbose_name='Прогресс')
    achievement = models.TextField(blank=True, verbose_name='Достижения')

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __str__(self):
        return f"{self.user} - {self.challenge}"
