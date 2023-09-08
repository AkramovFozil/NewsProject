from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.urls import reverse_lazy
# from django.views.generic import CreateView

from .forms import LoginForm, UseRegistrationForm, UserEditForm, ProfileEditForm


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Login muvaffaqiyatli amalga oshirildi!')
                else:
                    return HttpResponse('Sizning profilingiz faol holatda emas')
            else:
                return HttpResponse("login yoki parolingizda xatolik bor!")

    else:
        form = LoginForm()
        context = {
            'form': form
        }
    return render(request, 'registration/login.html', context)


def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home-page")


def dashboard(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        'user': user,
        'profile':profile,
    }
    return render(request, 'account/user_profile.html', context)


def user_register(request):
    if request.method == "POST":
        user_form = UseRegistrationForm(request.POST)
        if user_form.is_valid():
            news_user = user_form.save(commit=False)
            news_user.set_password(
                user_form.cleaned_data['password']
            )
            news_user.save()
            context = {
                'new_user': news_user
            }
            return render(request, 'account/register_done.html', context)
    else:
        user_form = UseRegistrationForm()
        context = {
            'form': user_form
        }
        return render(request, 'account/register.html', context)


def user_edit(request):

    if request.method == "POST":
        user_form = UserEditForm(instance=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES
                                       )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()


    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm()


        context = {
            'user_form': user_form,
            'profile_form': profile_form,

        }



    return render(request, 'account/profile_edit.html', context)



