from django.shortcuts import render, redirect
from .forms import PalabraForm
from django.http import JsonResponse

# Create your views here.
def ingreso_palabra(request):
    if request.method == 'POST':
        form = PalabraForm(request.POST)
        if form.is_valid():
            palabra = form.save()
            return JsonResponse({'message': f'La palabra "{palabra}" fue ingresada correctamente como {"palíndromo" if palabra.es_palindromo else "no palíndromo"}.'})
    
    return render(request, 'ingreso_palabra.html', {'form': form})