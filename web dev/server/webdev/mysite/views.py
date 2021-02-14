from django.shortcuts import render
from django.urls import reverse
from .models import Book, Publisher
from django.forms import ModelForm
from django.db.models import Q
import datetime
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'mysite/current_datetime.html', {'date': now})


def hour_ahead(request, time):
    now = datetime.datetime.now()
    hour_ahead = now + datetime.timedelta(hours=time)
    html = "<html><body>In %s hour, it will be %s</body></html>" % (time, hour_ahead)
    # assert False
    return HttpResponse(html)


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_naem__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
        # return HttpResponseRedirect(reverse(results))
    else:
        results = []
    return render(request, 'mysite/search.html', 
        {'results': results, 'query': query})

    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_date.get('sender', 'noreply@example.com')
            send_mail(f"Feedback from your site, topic: {topic}, {message}, {sender}, {['administraor@example.com']}")
            return HttpResponseRedirect(reverse('thanks'))
    form = ContactForm()
    return render(request, 'mysite/contact.html', {'form': form})


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city', 'state', 'country', 'website']


def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = PublisherForm()
        return render(request, 'mysite/add_publisher.html', {'form': form})


def thanks(request):
    return render(request, 'mysite/thanks.html')