from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

def index(request):
    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name="index.html"
    def post(self,request):
        return render(request)
    
    def get(self,request):
        nombre = "Araceli"
        edad = 49
        return render(request,self.template_name,{
            'nombre':nombre,
            'edad': edad
        })
    
    datos= dict,{
        'nombre': 'Araceli',
        'primer_apellido' : 'Salgado',
        'segundo_apellido': 'Camacho',
        'fecha_de_nacimiento': 1973,
        'celular': 33-1777-6502,
        'correo': "araceli.salgado.camacho@hpe.com",
        'domicio': "Periferico Sur 6570",
        'genero': "Femenino",
        'objetivo': "Desarrollo profesional",
        'salario_esperado': 50000-60000
    }
    skills= {
        'team work': "Team work",
        'project_management': "Project management",
        'english': "Advanced english level"
    }
    trabajos= dict,{
        'lugar_trabajo': "HP",
        'año_inicio': 2009,
        'año_fin': 2015,
        'puesto': "Supervisor",

        'lugar_trabajo': "HPE",
        'año_inicio': 2016,
        'año_fin': 2018,
        'puesto': "Purchasing contact"
    }

    print (datos, trabajos,skills)