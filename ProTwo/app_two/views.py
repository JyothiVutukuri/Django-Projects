from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import MyUser, Profile
from app_two.forms import FormOne, ProfileInForm, ProfileExtendForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def two_home(request):
    return render(request, "app_two/home.html")


def help(request):
    dict = {"my_variable": "Help page"}
    return render(request,"app_two/help.html",context = dict)


def users(request):
    u_dict = {"user": MyUser.objects.all()}
    return render(request, "app_two/mtv.html", context=u_dict)


def form_one(request):
    form = FormOne()

    if request.method == 'POST':
        form = FormOne(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            form.save(commit=True)
            return home(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'app_two/users.html', {'form': form})


def register(request):

    registered = False

    if request.method == 'POST':
        profile_in_form = ProfileInForm(request.POST)
        profile_extend_form = ProfileExtendForm(request.POST)

        if profile_in_form.is_valid() and profile_extend_form.is_valid():

            user = profile_in_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_extend_form.save(commit=False)
            profile.user = user

            if 'profile_photo' in request.FILES:
                print('found it')
                profile.profile_photo = request.FILES['profile_photo']

                profile.save()
            registered = True
        else:
            print(profile_in_form.errors, profile_extend_form.errors)

    else:
        profile_in_form = ProfileInForm()
        profile_extend_form = ProfileExtendForm()

    return render(request, 'register.html', {'registered': registered, 'profile_in_form': profile_in_form , 'profile_extend_form': profile_extend_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('YOU ARE INACTIVE')
        else:
            print('This username {} and password {} combination failed '.format(username, password))
            return HttpResponse('Invalid Credentials')
    else:
        return render(request, 'login.html')



