from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/inicio.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def formulario(request):
    if request.method == 'POST':
        curso = Curso(request.post['curso'],(request.post['camada']))
        curso.save()
        return render(reques, "AppCoder/inicio.html")
    return render(request, "AppCoder/formulario.html")

