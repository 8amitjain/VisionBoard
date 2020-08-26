from django.shortcuts import render, redirect

from .forms import ContactUsForm


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactUsForm()
    context = {
        'form': form,
    }
    return render(request, 'home/contact.html', context)


def faq(request):
    return render(request, 'home/faq.html')


def developer(request):
    return render(request, 'home/developer.html')

