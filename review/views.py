from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def external(request):
    inp= request.POST.get('param')
    out= run([sys.executable,'C:/Users/user/Desktop/New folder/CarParkProject/CarParkProject/main.py',inp],shell=False,stdout=PIPE)
    print(out)

    return render(request,'index.html',{'data1':out.stdout.decode('utf-8')})