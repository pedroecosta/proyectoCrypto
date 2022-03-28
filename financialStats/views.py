from django.http import HttpResponse
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from financialStats.models import Cypto, Cedear, opcionNegociable, FCI













def probandoTemplate(self):
    miHtml = open("C:/Users/PEDRO/Desktop/proyectoCrypto/financialStats/plantillas/template.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close() #Cerramos el archivo
    
    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
   
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    
    return HttpResponse(documento)