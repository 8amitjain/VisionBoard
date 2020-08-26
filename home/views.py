from django.shortcuts import render, redirect

from .forms import ContactUsForm


def home(request):
    return render(request, 'home/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})


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
