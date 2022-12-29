from django.shortcuts import render

# Create your views here.
def jp (request):
    d={'name':'Django'}
    return render(request,'jp.html',d)