from django.shortcuts import render


# Create your views here.

def register_user(request):
    return render(request, 'accounts/register-page.html')


def edit_user(request):
    return render(request, 'accounts/profile-edit-page.html')


def details_user(request):
    return render(request, 'accounts/profile-details-page.html')


def delete_user(request):
    return render(request, 'accounts/profile-delete-page.html')


def login_user(request):
    return render(request, 'accounts/login-page.html')
