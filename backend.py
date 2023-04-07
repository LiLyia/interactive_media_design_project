# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:04:33 2021

@author: Dell
"""
import path.py as p
from django.shortcuts import render
#from django.http import HttpResponse

def printer(request):
    start = request.GET['from']
    end = request.GET['to']
    if start == "South gate":
        start = 100
    else:
        start = int(start)
    if end == "South gate":
        end = 100
    else:
        end = int(end)
    p.main(start, end)
    text = p.textpath(p.minarray, start, end)
    return render(request,'printer.html',{'text': text})
