#Server
from django.http import HttpResponse, JsonResponse
from http import HTTPStatus

#Utilities
from datetime import datetime
import os

def status(request):
    try:
        return JsonResponse({
                'message': 'PlatziGram working properly.',
                'date': datetime.now().strftime('%b %dth, %Y - %H:%M Hrs'),
                'hostname':os.uname()[1]
            }, status=HTTPStatus.OK)
    except Exception as ex:
        print(ex)
        return JsonResponse({'message': 'An error'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

def challenge(request):
    try:
        response = dict()
        numbers = list()
        if len(request.GET) > 0 and request.GET['numbers']:
            numbers = request.GET['numbers']
            numbersInt = [ int(i) for i in numbers.split(',')]
            numbers = sorted(numbersInt)
            response = {
                'numbers': numbers
            }
        else:
            response = {
                'message': 'There are not numbers!'
            }

        return JsonResponse(response, status=HTTPStatus.OK)
    except Exception as ex:
        print(ex)
        return JsonResponse({'message': 'An error'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

def greeting(request, name, age):
    try:
        if age < 12:
            message = 'Sorry {name}, you are not allowed here!'.format(name=name)
        else:
            message = 'Hello {}!, Welcome to PlatziGram'.format(name)

        return JsonResponse({
                'message': message
            }, status=HTTPStatus.OK)
    except Exception as ex:
        print(ex)
        return JsonResponse({'message': 'An error'}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
     