from django.shortcuts import render


def pizzeria_listings(request):
    return render(request, 'pizzerias/pizzeria_list.html')
