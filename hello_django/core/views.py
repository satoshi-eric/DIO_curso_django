from django.shortcuts import render, HttpResponse

# Create your views here.

# Para passar parâmetros pela url, é necessário que o nome dos parâmetros da url sejam iguais aos parâmetros da função

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, num1, num2):
    return HttpResponse(f'<h1>{num1+num2}</h1>')

def subtracao(request, num1, num2):
    return HttpResponse(f'<h1>{num1-num2}</h1>')

def multiplicacao(request, num1, num2):
    return HttpResponse(f'<h1>{num1*num2}</h1>')

def divisao(request, num1, num2):
    try:
        return HttpResponse(f'<h1>{num1/num2}</h1>')
    except ZeroDivisionError:
        return HttpResponse('<h1>Divisão por Zero.</h1>')