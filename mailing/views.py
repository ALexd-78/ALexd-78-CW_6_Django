from django.shortcuts import render


def index(request):
    return render(request, 'mailing/index.html')


def get_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'User {name} with email {email} send message: {message}')
    return render(request, 'mailing/contacts.html')
