from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bot import type1

"""

@csrf_exempt
def command(request):

    if request.method == 'GET':
        data = request.GET
    else:
        return HttpResponse('GET only')

    print(json.dumps(data))
    return HttpResponse(json.dumps(data))
"""


@csrf_exempt
def command(request):    # to confirm

    if request.method != 'POST':
        return HttpResponse('NO')

    data = request.body.decode("utf-8")
    data = json.loads(data)
    print(data["user_name"])
    print(data["task"])
    print(data["user_id"])
    type1.send_nudes(data)
    return HttpResponse('')


@csrf_exempt
def command0(request):    # after creating task

    if request.method != 'POST':
        return HttpResponse('NO')

    data = request.body.decode("utf-8")
    data = json.loads(data)
    print(data["user_name"])
    print(data["task"])
    print(data["user_id"])
    print(data["deadline"])
    type1.send_nudes0(data)
    return HttpResponse('')


@csrf_exempt
def home_view(request):
    print('Home page')
    return HttpResponse('Home page')


