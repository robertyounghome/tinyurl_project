from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import TinyURL
from .forms import TinyURLForm
from pyshorteners import Shortener

def index(request):
    if request.method == 'POST':
        form = TinyURLForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            shortener = Shortener()
            short_url = shortener.tinyurl.short(long_url)
            TinyURL.objects.create(long_url=long_url, short_url=short_url)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TinyURLForm()

    urls = TinyURL.objects.all().order_by('-created_at')
    context = {'form': form, 'urls': urls}
    return render(request, 'tinyurl/index.html', context)
