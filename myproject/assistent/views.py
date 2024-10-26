# -- coding: utf8 --


import requests
from django.http import JsonResponse
from django.shortcuts import render
import json

from authentication.models import User
import g4f
from g4f.client import Client




def smart_assistent(messages):
    messages.insert(0, {'role': 'assistant', 'content': 'ок'})

    messages.insert(0, {'role': 'user', 'content': 'представь что ты умный помощник на сайте  где можно участвовать в корпоративных челленджах и командных соревнованиях, прокачивать командный дух и взаимодействовать с коллегами.Каждый сотрудник может создать свой профиль, устанавливать личные цели, участвовать в командных соревнованиях и отслеживать свои достижения.Платформа объединяет сотрудников, позволяя им не только ставить личные цели, но и участвовать в командных челленджах. Встроенный календарь корпоративных событий помогает отслеживать все предстоящие игры и активности.В итоге, это — пространство для взаимодействия, где можно бросать вызовы коллегам, следить за результатами друг друга, делиться опытом и делать рабочие будни интереснее и веселее через соревновательные активности!Цели проекта Укрепление команды — командные челленджи сближают сотрудников и  помогают лучше узнать друг друга, даже если они работают в разных отделах или городах. Повышение корпоративной культуры — для сотрудников ценно видеть,  что компания беспокоится о них, заботится об их здоровье и самочувствии.Повышение настроения сотрудников — участие во внерабочих  активностях помогает соблюдать work/life баланс, оставаться активным, достигать как рабочих, так и личных целей в игровой форме'})

    client = Client()

    response = client.chat.completions.create(
            messages=messages,
            model=g4f.models.default,
        )

    return response.choices[0].message.content

def get_answer(request):
    if request.method == 'GET':
        data = json.loads(request.body)

        resp = smart_assistent(data.get('messages'))
        return JsonResponse({'answer': resp}, status=200)


    return JsonResponse({'error': 'Invalid method. Only GET allowed.'}, status=405)
