from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.files.storage import FileSystemStorage
from .form import UserBioForm


def get_request_method(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a')
    b = request.GET.get('b')
    result = a + b
    context = {
        'a': a,
        'b': b,
        'result': result,
    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        'form': UserBioForm(),
    }
    return render(request, 'requestdataapp/user-form.html', context=context)


def upload_file(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        size_file = myfile.size
        print(size_file)
        if size_file < 10:
            file_name = fs.save(myfile.name, myfile)
            print(f'Saved file {file_name}')
            print(f'Файл {file_name} допустимого размера')
        else:
            print('Файл превышает допустимый размер в байтах')
            return render(request, 'requestdataapp/base.html')

    return render(request, 'requestdataapp/upload-file.html')
