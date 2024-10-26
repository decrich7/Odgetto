from django.urls import path
from .views import  GetAnswerView

urlpatterns = [
    path('get_answer/', GetAnswerView.as_view(), name='get_answer'),
]