from django.shortcuts import render, redirect


def aboutpage(request):
    return render(request, "about.html")


def servicepage(request):
    return render(request, "services.html")


def projectpage(request):
    return render(request, 'projects.html')


def blogpage(request):
    return render(request, 'blog.html')