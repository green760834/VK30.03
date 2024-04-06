from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import vk
import random

session = vk.Session(access_token="")
vk_api

@csrf_exempt
def index(request):
    return HttpResponse("6ded20a6") 