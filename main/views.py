from django.shortcuts import render


# Create your views here.
def home(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/home.html', {'title': 'Главная страница'})


