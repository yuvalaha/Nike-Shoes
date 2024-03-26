from django.shortcuts import render


def home(request):
    context = {"active": "home"}
    return render(request, "home.html", context=context)


