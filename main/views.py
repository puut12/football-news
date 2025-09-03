from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406414012',
        'name': 'Putri Hamidah Riyanto',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)