from django.shortcuts import render
from .models import Contact
import requests, json


# Create your views here.
def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        print(joke)
        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)

    else:
        firstname = 'Daniel'
        lastname = 'K'
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        print(joke)
        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)


def index2(request):
    return render(request, 'mysite/index2.html')


def contact(request):
    print(request.method)
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        print(request.POST.get('email'))
        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')


def portofolio(request):
    return render(request, 'mysite/portofolio.html')
