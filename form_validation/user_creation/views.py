from django.shortcuts import render, redirect
from .form import SignUpForm


# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-user')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})
