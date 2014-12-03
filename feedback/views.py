from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm

# Create your views here.

def feed(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thankyou.html",)
    else:
        form = FeedbackForm()
    return render(request, "feedback.html", {'form': form})

