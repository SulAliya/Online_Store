from django.shortcuts import render
from django.utils.translation.trans_real import catalog


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('datas.txt', "w") as file:
            file.write(f'{name}, {phone}, {message}')
    return render(request, 'contacts.html')

