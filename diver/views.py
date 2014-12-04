from django.shortcuts import render, redirect
from .models import Diver
from .forms import DiverModelForm
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def diver_list(request):
    divers = Diver.objects.all()
    return render(request, "diver_list.html", {"divers": divers})


def diver_add(request):
    if request.method == "POST":
        print request.POST
        form = DiverModelForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            firstname = form.cleaned_data.get('firstName', None)
            lastname = form.cleaned_data.get('lastName', None)
            password = form.cleaned_data.get('password', None)
            passwordconfirm = form.cleaned_data.get('passwordConfirm', None)
            if password != None and password == passwordconfirm:
                user = User(username=username,
                            first_name=firstname,
                            last_name=lastname,
                            password=password
                            )
                user.save()
                d = Diver(diver=user,
                          phone=form.cleaned_data.get('phone', None),
                          age=form.cleaned_data.get('age', None),
                          size=form.cleaned_data.get('size', None)
                )
                d.save()
                return redirect('diver_list')
        else:
            return render(request, "add.html", {"form": form})
    else:
        form = DiverModelForm()
        return render(request, "add.html", {"form": form})
    return HttpResponse("Entered request.method == post and got no answer")
