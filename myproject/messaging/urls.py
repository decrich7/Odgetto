from django.urls import path
from .views import SendMessageView

urlpatterns = [
    path('send_message/', SendMessageView.as_view(), name='send_message'),
]