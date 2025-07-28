from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Replace with your real template later
