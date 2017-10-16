from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """User logout"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """Register new user"""
    if request.method != 'POST':
        # Display an empty form
        form = UserCreationForm()
    else:
        # Render a form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # login in user and redirect him to home page
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
