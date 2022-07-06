from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'core/inicio_Catalogo.html')

def create_acount(request):
    return render(request,'core/create_acount_form.html' )

def inicio_sesion(request):
    return render(request,'core/inicio_sesion.html' )