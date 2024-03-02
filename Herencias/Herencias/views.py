from django.shortcuts import render


def inicio(request):
  return render(request, 'index.html', {})

def blog(request):
  return render(request, "blog.html", {})

def nosotros(request):
  return render(request, "nosotros.html", {})

def contacto(request):
  return render(request, "contacto.html", {})

def servicios(request):
  return render(request, "servicios.html", {})