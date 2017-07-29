from django.shortcuts import render


def index(request):
    return render(request, 'myprofile/home.html')


def contact(request):
    return render(request, 'myprofile/basic.html', {
        'content': ['To contact me drop me an email on:', 'email@email.com']
    })
