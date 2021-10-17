from django.shortcuts import render, redirect # when the sign up is finished redirect the user
from django.contrib.auth import login #authenticate the user
from django.contrib.auth.forms import UserCreationForm #default form for creating user in the BACK END

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})