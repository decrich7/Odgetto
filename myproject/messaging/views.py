import requests
from django.http import JsonResponse
from django.shortcuts import render
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from authentication.models import User
from decouple import config



class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = json.loads(request.body)
        message = data.get('message')
        user_id = data.get('user_id')
        user = User.objects.get(id=user_id)

        if not message or not user_id:
            return JsonResponse({'error': 'Missing message or user_id'}, status=400)

        BOT_TOKEN = config('TOKEN')

        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        response = requests.post(url, data={'chat_id': user.tg_id, 'text': message})

        return JsonResponse({'success': 'Message send successfully'}, status=200)






#
# def send_message(request):
#     if request.method == 'GET':
#         try:
#             data = json.loads(request.body)
#             message = data.get('message')
#             user_id = data.get('user_id')
#             user = User.objects.get(id=user_id)
#
#             if not message or not user_id:
#                 return JsonResponse({'error': 'Missing message or user_id'}, status=400)
#
#             BOT_TOKEN = '7564082109:AAFrn4G_3h0rHqjogJo4UyXuXJB6Gda-zDU'
#             url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
#             response = requests.post(url, data={'chat_id': user.tg_id, 'text': message})
#
#             return JsonResponse({'success': 'Message send successfully'}, status=200)
#
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#
#     return JsonResponse({'error': 'Invalid method. Only GET allowed.'}, status=405)