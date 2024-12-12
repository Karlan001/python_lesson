from django.urls import path, include
from .views import get_request_method, user_form, upload_file

app_name = 'requestdataapp'
urlpatterns = [
    path('get/', get_request_method, name='get-view'),
    path('bio/', user_form, name='user-form'),
    path('file/', upload_file, name='upload-file'),
]
