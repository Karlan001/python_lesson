import datetime
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def get_response_name_middleware(get_response: HttpResponse):
    def middleware(request: HttpRequest):
        print("before initialization")

        request.user_agent = request.META
        response = get_response(request)

        print("after initialization")

        return response

    return middleware


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count_response = 0
        self.count_request = 0
        self.count_exception = 0
        self.user_info = {}

    def __call__(self, request):
        time_delta = 5
        response = self.get_response(request)
        time_request = datetime.datetime.now()
        user_address = request.META['REMOTE_ADDR']
        if not self.user_info:
            print('Запросов еще не было')
        else:
            if (time_request - self.user_info['time_request']) < datetime.timedelta(seconds=time_delta) \
                    and user_address == self.user_info['user_address']:
                print(f'Пользователь {request.META["REMOTE_ADDR"]} слишком часто отправляет запросы')
                return render(request, 'requestdataapp/base.html')

        self.user_info = {'user_address': user_address, 'time_request': time_request}
        self.count_request += 1
        print(f'count request = {self.count_request}')
        self.count_response += 1
        print(f'count response = {self.count_response}')

        return response
