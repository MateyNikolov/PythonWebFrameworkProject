from django.shortcuts import render


def show_this_page(req):
    return render(req, 'core/home.html')

